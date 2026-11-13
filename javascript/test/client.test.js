import test from "node:test";
import assert from "node:assert/strict";
import {
  LichessClient, CrawloraClientError, CrawloraNetworkError,
  CrawloraServerError, groups, operations, operationCount
} from "../src/index.js";

const json = (data, status = 200, headers = {}) => new Response(JSON.stringify(data), {
  status, headers: { "content-type": "application/json", ...headers }
});

test("exports only this platform and exposes direct and grouped methods", async () => {
  const client = new LichessClient({ apiKey: "test-key", fetch: async () => json({ ok: true }) });
  assert.equal(operationCount, Object.keys(operations).length);
  assert.deepEqual(Object.keys(groups), ["lichess"]);
  assert.equal(typeof client["cloudEval"], "function");
  assert.equal(typeof client["lichess"]["cloudEval"], "function");
});

test("serializes required query/path values, adds API key and platform User-Agent", async () => {
  let seen;
  const client = new LichessClient({ apiKey: "secret", fetch: async (url, init) => {
    seen = { url: String(url), headers: init.headers };
    return json({ ok: true });
  } });
  await client.request("lichess-cloud-eval", {"fen": "sample"});
  assert.match(seen.url, /\/lichess\/cloud\-eval/);
  assert.equal(seen.headers["x-api-key"], "secret");
  assert.equal(seen.headers["user-agent"], "crawlora-lichess-js/0.1.0");
});

test("allows caller User-Agent override and response text mode", async () => {
  let seen;
  const client = new LichessClient({ apiKey: "key", userAgent: "custom-agent", fetch: async (_url, init) => {
    seen = init.headers;
    return new Response("caption text", { headers: { "content-type": "text/plain" } });
  } });
  const result = await client.request("lichess-cloud-eval", {"fen": "sample"}, { responseType: "text" });
  assert.equal(seen["user-agent"], "custom-agent");
  assert.equal(result, "caption text");

  const rawFeed = "1~home|2~away\n";
  const autoClient = new LichessClient({ fetch: async () => new Response(rawFeed, {
    headers: { "content-type": "text/plain" }
  }) });
  assert.equal(await autoClient.request("lichess-cloud-eval", {"fen": "sample"}), rawFeed);
});

test("maps API errors and retries server failures", async () => {
  let calls = 0;
  const client = new LichessClient({ apiKey: "key", retries: 1, retryDelay: 0, fetch: async () => {
    calls++;
    return calls === 1 ? json({ msg: "try again" }, 503) : json({ ok: true });
  } });
  assert.deepEqual(await client.request("lichess-cloud-eval", {"fen": "sample"}), { ok: true });
  assert.equal(calls, 2);

  const bad = new LichessClient({ fetch: async () => json({ msg: "bad input" }, 400) });
  await assert.rejects(bad.request("lichess-cloud-eval", {"fen": "sample"}), CrawloraClientError);
  const down = new LichessClient({ fetch: async () => json({ msg: "down" }, 503) });
  await assert.rejects(down.request("lichess-cloud-eval", {"fen": "sample"}), CrawloraServerError);
});

test("reports timeout and caller cancellation as network errors", async () => {
  const hanging = (_url, { signal }) => new Promise((_resolve, reject) => {
    signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true });
  });
  const timed = new LichessClient({ timeout: 5, fetch: hanging });
  await assert.rejects(timed.request("lichess-cloud-eval", {"fen": "sample"}), CrawloraNetworkError);

  const controller = new AbortController();
  const aborted = new LichessClient({ fetch: hanging });
  const pending = aborted.request("lichess-cloud-eval", {"fen": "sample"}, { signal: controller.signal });
  controller.abort();
  await assert.rejects(pending, CrawloraNetworkError);
});

# @crawlora-org/lichess — Lichess API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Lichess API.
It exposes 11 API endpoints for puzzles, tablebases, tournaments, cloud evaluations, and public event listings through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-javascript-homepage). It does not run a browser or scrape Lichess locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Lichess or its owners.

## Install

```sh
npm install @crawlora-org/lichess
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { LichessClient } from "@crawlora-org/lichess";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LichessClient({ apiKey });
const result1 = await client.enums({});
console.log(result1);
const result2 = await client.puzzleDaily({});
console.log(result2);
```

The client also exports `Client` as an alias for `LichessClient`. Operation
methods are available directly in camelCase and through the `lichess`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-lichess/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Lichess API endpoints

This package exposes each route below as a direct method and through the `lichess` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/lichess/cloud-eval` | `lichess-cloud-eval` | Get a cached Lichess cloud evaluation |
| `GET` | `/lichess/enums` | `lichess-enums` | List Lichess public read enums |
| `GET` | `/lichess/puzzle` | `lichess-puzzle` | Get a public Lichess puzzle |
| `GET` | `/lichess/puzzle/batch` | `lichess-puzzle-batch` | Get a Lichess puzzle batch by theme |
| `GET` | `/lichess/puzzle/daily` | `lichess-puzzle-daily` | Lichess daily puzzle |
| `GET` | `/lichess/puzzle/many` | `lichess-puzzle-many` | Get multiple Lichess puzzles by ID |
| `GET` | `/lichess/puzzle/next` | `lichess-puzzle-next` | Get a Lichess puzzle by source filters |
| `GET` | `/lichess/puzzle/themes` | `lichess-puzzle-themes` | Discover Lichess puzzle themes |
| `GET` | `/lichess/simuls` | `lichess-simuls` | List public Lichess simultaneous exhibitions |
| `GET` | `/lichess/tablebase` | `lichess-tablebase` | Query the Lichess tablebase |
| `GET` | `/lichess/version` | `lichess-version` | Get the Lichess server version |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.

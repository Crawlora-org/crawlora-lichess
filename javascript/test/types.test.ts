import { LichessClient } from "../src/index.js";

const client = new LichessClient({ apiKey: "test-key" });
void client.cloudEval({"fen": "sample"});
void client.request("lichess-cloud-eval", {"fen": "sample"});
const streamResponse: Promise<Response> = client.request("lichess-cloud-eval", {"fen": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("lichess-cloud-eval", {"fen": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.cloudEval({"fen": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("lichess-cloud-eval", {"fen": "sample", "multiPv": 1, "variant": "standard"}, { responseType: "text" });
const rawText: Promise<string> = client.request("lichess-cloud-eval", {"fen": "sample"}, { responseType: "text" });
void rawText;


void client.enums();
void client.request("lichess-enums");
// @ts-expect-error The selected operation requires its documented params.
void client.cloudEval();

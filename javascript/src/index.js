import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class LichessClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-lichess-js/0.1.0" });
    this["cloudEval"] = (...args) => this.request("lichess-cloud-eval", ...args);
    this["enums"] = (...args) => this.request("lichess-enums", ...args);
    this["puzzle"] = (...args) => this.request("lichess-puzzle", ...args);
    this["puzzleBatch"] = (...args) => this.request("lichess-puzzle-batch", ...args);
    this["puzzleDaily"] = (...args) => this.request("lichess-puzzle-daily", ...args);
    this["puzzleMany"] = (...args) => this.request("lichess-puzzle-many", ...args);
    this["puzzleNext"] = (...args) => this.request("lichess-puzzle-next", ...args);
    this["puzzleThemes"] = (...args) => this.request("lichess-puzzle-themes", ...args);
    this["simuls"] = (...args) => this.request("lichess-simuls", ...args);
    this["tablebase"] = (...args) => this.request("lichess-tablebase", ...args);
    this["version"] = (...args) => this.request("lichess-version", ...args);
  }
}

export { LichessClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default LichessClient;

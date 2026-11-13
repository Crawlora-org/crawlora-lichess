import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class LichessClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  cloudEval(params: OperationParamsMap["lichess-cloud-eval"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  enums(params?: OperationParamsMap["lichess-enums"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzle(params: OperationParamsMap["lichess-puzzle"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleBatch(params: OperationParamsMap["lichess-puzzle-batch"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleDaily(params?: OperationParamsMap["lichess-puzzle-daily"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleMany(params: OperationParamsMap["lichess-puzzle-many"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleNext(params?: OperationParamsMap["lichess-puzzle-next"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  puzzleThemes(params?: OperationParamsMap["lichess-puzzle-themes"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  simuls(params?: OperationParamsMap["lichess-simuls"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tablebase(params: OperationParamsMap["lichess-tablebase"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  version(params?: OperationParamsMap["lichess-version"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  cloudEval(params: OperationParamsMap["lichess-cloud-eval"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  enums(params?: OperationParamsMap["lichess-enums"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzle(params: OperationParamsMap["lichess-puzzle"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleBatch(params: OperationParamsMap["lichess-puzzle-batch"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleDaily(params?: OperationParamsMap["lichess-puzzle-daily"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleMany(params: OperationParamsMap["lichess-puzzle-many"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleNext(params?: OperationParamsMap["lichess-puzzle-next"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  puzzleThemes(params?: OperationParamsMap["lichess-puzzle-themes"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  simuls(params?: OperationParamsMap["lichess-simuls"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tablebase(params: OperationParamsMap["lichess-tablebase"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  version(params?: OperationParamsMap["lichess-version"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  cloudEval(...args: OperationRequestArgs<"lichess-cloud-eval">): Promise<OperationResponseMap["lichess-cloud-eval"]>;
  enums(...args: OperationRequestArgs<"lichess-enums">): Promise<OperationResponseMap["lichess-enums"]>;
  puzzle(...args: OperationRequestArgs<"lichess-puzzle">): Promise<OperationResponseMap["lichess-puzzle"]>;
  puzzleBatch(...args: OperationRequestArgs<"lichess-puzzle-batch">): Promise<OperationResponseMap["lichess-puzzle-batch"]>;
  puzzleDaily(...args: OperationRequestArgs<"lichess-puzzle-daily">): Promise<OperationResponseMap["lichess-puzzle-daily"]>;
  puzzleMany(...args: OperationRequestArgs<"lichess-puzzle-many">): Promise<OperationResponseMap["lichess-puzzle-many"]>;
  puzzleNext(...args: OperationRequestArgs<"lichess-puzzle-next">): Promise<OperationResponseMap["lichess-puzzle-next"]>;
  puzzleThemes(...args: OperationRequestArgs<"lichess-puzzle-themes">): Promise<OperationResponseMap["lichess-puzzle-themes"]>;
  simuls(...args: OperationRequestArgs<"lichess-simuls">): Promise<OperationResponseMap["lichess-simuls"]>;
  tablebase(...args: OperationRequestArgs<"lichess-tablebase">): Promise<OperationResponseMap["lichess-tablebase"]>;
  version(...args: OperationRequestArgs<"lichess-version">): Promise<OperationResponseMap["lichess-version"]>;
}
export { LichessClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default LichessClient;

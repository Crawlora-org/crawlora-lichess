# Lichess API endpoint reference and client usage

This reference lists all 11 public Lichess API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/lichess`, `crawlora-lichess`, and `crawlora-lichess` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Lichess locally; Crawlora is independent from and not endorsed by Lichess or its owners.

The package tracks the public API contract revision `sha256:8d6a06c89f86c9115cf49df6128b8e3e4f83d8743771a5788f13a0cde99e45af` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `lichess`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `cloudEval` | `cloud_eval` | `lichess.cloud_eval` | `GET /lichess/cloud-eval` | `fen` (query, required), `multiPv` (query, optional), `variant` (query, optional; values: `standard`, `chess960`, `crazyhouse`, `antichess`, `atomic`, `horde`, `kingOfTheHill`, `racingKings`, `threeCheck`, `fromPosition`) | Get a cached Lichess cloud evaluation |
| `enums` | `enums` | `lichess.enums` | `GET /lichess/enums` | — | List Lichess public read enums |
| `puzzle` | `puzzle` | `lichess.puzzle` | `GET /lichess/puzzle` | `id` (query, required) | Get a public Lichess puzzle |
| `puzzleBatch` | `puzzle_batch` | `lichess.puzzle_batch` | `GET /lichess/puzzle/batch` | `angle` (query, required), `difficulty` (query, optional; values: `easiest`, `easier`, `normal`, `harder`, `hardest`), `nb` (query, optional), `color` (query, optional; values: `white`, `black`) | Get a Lichess puzzle batch by theme |
| `puzzleDaily` | `puzzle_daily` | `lichess.puzzle_daily` | `GET /lichess/puzzle/daily` | — | Lichess daily puzzle |
| `puzzleMany` | `puzzle_many` | `lichess.puzzle_many` | `GET /lichess/puzzle/many` | `ids` (query, required) | Get multiple Lichess puzzles by ID |
| `puzzleNext` | `puzzle_next` | `lichess.puzzle_next` | `GET /lichess/puzzle/next` | `angle` (query, optional), `difficulty` (query, optional; values: `easiest`, `easier`, `normal`, `harder`, `hardest`), `color` (query, optional; values: `white`, `black`) | Get a Lichess puzzle by source filters |
| `puzzleThemes` | `puzzle_themes` | `lichess.puzzle_themes` | `GET /lichess/puzzle/themes` | — | Discover Lichess puzzle themes |
| `simuls` | `simuls` | `lichess.simuls` | `GET /lichess/simuls` | — | List public Lichess simultaneous exhibitions |
| `tablebase` | `tablebase` | `lichess.tablebase` | `GET /lichess/tablebase` | `variant` (query, required; values: `standard`, `atomic`, `antichess`), `fen` (query, required), `dtc` (query, optional; values: `never`, `auxiliary`, `always`) | Query the Lichess tablebase |
| `version` | `version` | `lichess.version` | `GET /lichess/version` | — | Get the Lichess server version |

## Client forms

- JavaScript: import `LichessClient` (also exported as `Client`) from `@crawlora-org/lichess`; use `new LichessClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `LichessClient` (also exported as `Client`) from `crawlora_lichess`; use `with LichessClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncLichessClient`, used with `async with` and `await`.
- Rust: add `crawlora-lichess` with Cargo; import `Client` and the generated operation parameter struct, then call `client.lichess.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-lichess/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.

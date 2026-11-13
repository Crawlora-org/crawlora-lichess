# Crawlora Lichess Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lichess | `lichess.cloud_eval` | `lichess-cloud-eval` | `GET /lichess/cloud-eval` | `fen` (query String required)<br>`multiPv` (query i64)<br>`variant` (query String enum{standard, chess960, crazyhouse, antichess, atomic, horde, kingOfTheHill, racingKings, threeCheck, fromPosition}) | `ApiKeyAuth` | `LichessCloudEvalResponse` |  |
| lichess | `lichess.enums` | `lichess-enums` | `GET /lichess/enums` | none | `ApiKeyAuth` | `LichessEnumsResponse` |  |
| lichess | `lichess.puzzle` | `lichess-puzzle` | `GET /lichess/puzzle` | `id` (query String required) | `ApiKeyAuth` | `LichessPuzzleResponse` |  |
| lichess | `lichess.puzzle_batch` | `lichess-puzzle-batch` | `GET /lichess/puzzle/batch` | `angle` (query String required)<br>`difficulty` (query String enum{easiest, easier, normal, harder, hardest})<br>`nb` (query i64)<br>`color` (query String enum{white, black}) | `ApiKeyAuth` | `LichessPuzzleBatchResponse` |  |
| lichess | `lichess.puzzle_daily` | `lichess-puzzle-daily` | `GET /lichess/puzzle/daily` | none | `ApiKeyAuth` | `LichessPuzzleDailyResponse` |  |
| lichess | `lichess.puzzle_many` | `lichess-puzzle-many` | `GET /lichess/puzzle/many` | `ids` (query String required) | `ApiKeyAuth` | `LichessPuzzleManyResponse` |  |
| lichess | `lichess.puzzle_next` | `lichess-puzzle-next` | `GET /lichess/puzzle/next` | `angle` (query String)<br>`difficulty` (query String enum{easiest, easier, normal, harder, hardest})<br>`color` (query String enum{white, black}) | `ApiKeyAuth` | `LichessPuzzleNextResponse` |  |
| lichess | `lichess.puzzle_themes` | `lichess-puzzle-themes` | `GET /lichess/puzzle/themes` | none | `ApiKeyAuth` | `LichessPuzzleThemesResponse` |  |
| lichess | `lichess.simuls` | `lichess-simuls` | `GET /lichess/simuls` | none | `ApiKeyAuth` | `LichessSimulsResponse` |  |
| lichess | `lichess.tablebase` | `lichess-tablebase` | `GET /lichess/tablebase` | `variant` (query String enum{standard, atomic, antichess} required)<br>`fen` (query String required)<br>`dtc` (query String enum{never, auxiliary, always}) | `ApiKeyAuth` | `LichessTablebaseResponse` |  |
| lichess | `lichess.version` | `lichess-version` | `GET /lichess/version` | none | `ApiKeyAuth` | `LichessVersionResponse` |  |

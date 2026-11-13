# Crawlora Lichess JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lichess | `lichess.cloudEval` | `lichess-cloud-eval` | `GET /lichess/cloud-eval` | `fen` (query string required)<br>`multiPv` (query number)<br>`variant` (query "standard" \| "chess960" \| "crazyhouse" \| "antichess" \| "atomic" \| "horde" \| "kingOfTheHill" \| "racingKings" \| "threeCheck" \| "fromPosition") | `ApiKeyAuth` | `LichessCloudEvalResponse` |  |
| lichess | `lichess.enums` | `lichess-enums` | `GET /lichess/enums` | none | `ApiKeyAuth` | `LichessEnumsResponse` |  |
| lichess | `lichess.puzzle` | `lichess-puzzle` | `GET /lichess/puzzle` | `id` (query string required) | `ApiKeyAuth` | `LichessPuzzleResponse` |  |
| lichess | `lichess.puzzleBatch` | `lichess-puzzle-batch` | `GET /lichess/puzzle/batch` | `angle` (query string required)<br>`difficulty` (query "easiest" \| "easier" \| "normal" \| "harder" \| "hardest")<br>`nb` (query number)<br>`color` (query "white" \| "black") | `ApiKeyAuth` | `LichessPuzzleBatchResponse` |  |
| lichess | `lichess.puzzleDaily` | `lichess-puzzle-daily` | `GET /lichess/puzzle/daily` | none | `ApiKeyAuth` | `LichessPuzzleDailyResponse` |  |
| lichess | `lichess.puzzleMany` | `lichess-puzzle-many` | `GET /lichess/puzzle/many` | `ids` (query string required) | `ApiKeyAuth` | `LichessPuzzleManyResponse` |  |
| lichess | `lichess.puzzleNext` | `lichess-puzzle-next` | `GET /lichess/puzzle/next` | `angle` (query string)<br>`difficulty` (query "easiest" \| "easier" \| "normal" \| "harder" \| "hardest")<br>`color` (query "white" \| "black") | `ApiKeyAuth` | `LichessPuzzleNextResponse` |  |
| lichess | `lichess.puzzleThemes` | `lichess-puzzle-themes` | `GET /lichess/puzzle/themes` | none | `ApiKeyAuth` | `LichessPuzzleThemesResponse` |  |
| lichess | `lichess.simuls` | `lichess-simuls` | `GET /lichess/simuls` | none | `ApiKeyAuth` | `LichessSimulsResponse` |  |
| lichess | `lichess.tablebase` | `lichess-tablebase` | `GET /lichess/tablebase` | `variant` (query "standard" \| "atomic" \| "antichess" required)<br>`fen` (query string required)<br>`dtc` (query "never" \| "auxiliary" \| "always") | `ApiKeyAuth` | `LichessTablebaseResponse` |  |
| lichess | `lichess.version` | `lichess-version` | `GET /lichess/version` | none | `ApiKeyAuth` | `LichessVersionResponse` |  |

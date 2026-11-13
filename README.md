# Lichess clients for Crawlora

Official Crawlora client packages for the hosted Lichess API. Access 11 API endpoints covering puzzles, tablebases, tournaments, cloud evaluations, and public event listings from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Lichess locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Lichess or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/lichess`](javascript/README.md)
- Python: [`crawlora-lichess`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-lichess`](go.mod)
- Ruby: [`crawlora-lichess`](ruby/README.md)
- Java: [`net.crawlora:crawlora-lichess:0.1.0`](java/README.md)
- PHP: [`crawlora/lichess`](php/README.md)
- Rust: [`crawlora-lichess`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 11 selected public Lichess API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).

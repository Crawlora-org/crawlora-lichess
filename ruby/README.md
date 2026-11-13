# Crawlora Lichess API client for Ruby (`crawlora-lichess`)

This Ruby gem calls Crawlora's hosted Lichess API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering puzzles, tablebases, tournaments, cloud evaluations, and public event listings; it does not call or scrape Lichess directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-lichess"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/lichess"

client = Crawlora::Lichess::Client.new
result = client.request("lichess-cloud-eval", JSON.parse("{\"fen\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 11 API operations.

```ruby
client = Crawlora::Lichess::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Lichess API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-lichess) for account setup, the API operation reference, and release history.

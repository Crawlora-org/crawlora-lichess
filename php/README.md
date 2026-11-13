# Crawlora Lichess API client for PHP (`crawlora/lichess`)

This PHP package calls Crawlora's hosted Lichess API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering puzzles, tablebases, tournaments, cloud evaluations, and public event listings. It does not call or scrape Lichess directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/lichess
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Lichess\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("lichess-cloud-eval", ['fen' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 11 API operations.

## Supported Lichess API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-lichess). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md).

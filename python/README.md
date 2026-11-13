# crawlora-lichess — Lichess API client for Python

Python client for Crawlora's hosted Lichess API. It exposes 11 API endpoints covering puzzles, tablebases, tournaments, cloud evaluations, and public event listings. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-python-homepage); the package does not run a browser or scrape
Lichess locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Lichess or its owners.

## Install

```sh
python -m pip install crawlora-lichess
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=lichess-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_lichess import LichessClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with LichessClient(api_key=api_key) as client:
    result_1 = client.enums()
    print(result_1)
    result_2 = client.puzzle_daily()
    print(result_2)
```

The package also exports `Client` as an alias for `LichessClient`. Operation
methods are available directly in snake_case and through the `lichess`
group. The async package client is `AsyncLichessClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-lichess/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_lichess import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.enums()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-lichess/blob/main/examples/python.py) for a complete usage example.

## Supported Lichess API endpoints

This package exposes every route below through direct snake_case methods and the `lichess` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-lichess/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.

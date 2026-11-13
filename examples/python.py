import os

from crawlora_lichess import LichessClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with LichessClient(api_key=api_key) as client:
    enums = client.enums()
    print('enums', enums)
    puzzle_daily = client.puzzle_daily()
    print('puzzle_daily', puzzle_daily)

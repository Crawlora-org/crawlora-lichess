"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class LichessClient(CrawloraClient):
    """Synchronous Lichess API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-lichess-python/0.1.0')
        super().__init__(*args, **kwargs)

    def cloud_eval(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-cloud-eval', params, response_type=response_type, timeout=timeout, headers=headers)

    def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_batch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle-batch', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_daily(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle-daily', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_many(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle-many', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_next(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle-next', params, response_type=response_type, timeout=timeout, headers=headers)

    def puzzle_themes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-puzzle-themes', params, response_type=response_type, timeout=timeout, headers=headers)

    def simuls(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-simuls', params, response_type=response_type, timeout=timeout, headers=headers)

    def tablebase(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-tablebase', params, response_type=response_type, timeout=timeout, headers=headers)

    def version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lichess-version', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncLichessClient(AsyncCrawloraClient):
    """Asynchronous Lichess API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-lichess-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def cloud_eval(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-cloud-eval', params, response_type=response_type, timeout=timeout, headers=headers)

    async def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_batch(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle-batch', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_daily(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle-daily', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_many(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle-many', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_next(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle-next', params, response_type=response_type, timeout=timeout, headers=headers)

    async def puzzle_themes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-puzzle-themes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def simuls(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-simuls', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tablebase(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-tablebase', params, response_type=response_type, timeout=timeout, headers=headers)

    async def version(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lichess-version', params, response_type=response_type, timeout=timeout, headers=headers)

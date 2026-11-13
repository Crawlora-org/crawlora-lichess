"""Typed Lichess client for the Crawlora hosted API."""

from .platform import LichessClient, AsyncLichessClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = LichessClient
AsyncClient = AsyncLichessClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Lichess'
PLATFORM = 'lichess'
CONTRACT_REVISION = 'sha256:8d6a06c89f86c9115cf49df6128b8e3e4f83d8743771a5788f13a0cde99e45af'

__all__ = [
    "LichessClient", "AsyncLichessClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]

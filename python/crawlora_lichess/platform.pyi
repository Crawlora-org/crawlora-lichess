from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelLichessServerVersionResponse = TypedDict('ModelLichessServerVersionResponse', {
    'server': NotRequired[ModelLichessServerVersion],
    'source_url': NotRequired[str],
}, total=False)

ModelLichessServerVersion = TypedDict('ModelLichessServerVersion', {
    'commit': NotRequired[str],
    'date': NotRequired[str],
}, total=False)

ModelLichessResponse = TypedDict('ModelLichessResponse', {
    'data': NotRequired[Any],
    'source_url': NotRequired[str],
}, total=False)

ModelLichessEnumsResponse = TypedDict('ModelLichessEnumsResponse', {
    'cloud_evaluation_default_variant': NotRequired[str],
    'cloud_evaluation_variants': NotRequired[list[str]],
    'puzzle_angle': NotRequired[str],
    'puzzle_batch_sizes': NotRequired[dict[str, Any]],
    'puzzle_colors': NotRequired[list[str]],
    'puzzle_difficulties': NotRequired[list[str]],
    'standard_dtc': NotRequired[list[str]],
    'tablebase_variants': NotRequired[list[str]],
}, total=False)

LichessCloudEvalResponse = Any
LichessCloudEvalParams = TypedDict('LichessCloudEvalParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'fen': Required[str],
    'multiPv': NotRequired[int],
    'variant': NotRequired[Literal['standard', 'chess960', 'crazyhouse', 'antichess', 'atomic', 'horde', 'kingOfTheHill', 'racingKings', 'threeCheck', 'fromPosition']],
}, total=False)

LichessEnumsResponse = Any
LichessEnumsParams = TypedDict('LichessEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

LichessPuzzleResponse = Any
LichessPuzzleParams = TypedDict('LichessPuzzleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

LichessPuzzleBatchResponse = ModelAppResponse
LichessPuzzleBatchParams = TypedDict('LichessPuzzleBatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'angle': Required[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'nb': NotRequired[int],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleDailyResponse = Any
LichessPuzzleDailyParams = TypedDict('LichessPuzzleDailyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

LichessPuzzleManyResponse = ModelAppResponse
LichessPuzzleManyParams = TypedDict('LichessPuzzleManyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'ids': Required[str],
}, total=False)

LichessPuzzleNextResponse = Any
LichessPuzzleNextParams = TypedDict('LichessPuzzleNextParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'angle': NotRequired[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleThemesResponse = Any
LichessPuzzleThemesParams = TypedDict('LichessPuzzleThemesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

LichessSimulsResponse = Any
LichessSimulsParams = TypedDict('LichessSimulsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

LichessTablebaseResponse = Any
LichessTablebaseParams = TypedDict('LichessTablebaseParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'variant': Required[Literal['standard', 'atomic', 'antichess']],
    'fen': Required[str],
    'dtc': NotRequired[Literal['never', 'auxiliary', 'always']],
}, total=False)

LichessVersionResponse = Any
LichessVersionParams = TypedDict('LichessVersionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class LichessGroup:
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalStreamParams]) -> BinaryIO: ...
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalTextResponseParams]) -> str: ...
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalDefaultParams]) -> LichessCloudEvalResponse: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsDefaultParams]) -> LichessEnumsResponse: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleTextResponseParams]) -> str: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleDefaultParams]) -> LichessPuzzleResponse: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchTextResponseParams]) -> str: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchDefaultParams]) -> LichessPuzzleBatchResponse: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyTextResponseParams]) -> str: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyDefaultParams]) -> LichessPuzzleDailyResponse: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyTextResponseParams]) -> str: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyDefaultParams]) -> LichessPuzzleManyResponse: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextTextResponseParams]) -> str: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextDefaultParams]) -> LichessPuzzleNextResponse: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesTextResponseParams]) -> str: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesDefaultParams]) -> LichessPuzzleThemesResponse: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsStreamParams]) -> BinaryIO: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsTextResponseParams]) -> str: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsDefaultParams]) -> LichessSimulsResponse: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseStreamParams]) -> BinaryIO: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseTextResponseParams]) -> str: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseDefaultParams]) -> LichessTablebaseResponse: ...
    @overload
    def version(self, **params: Unpack[LichessVersionStreamParams]) -> BinaryIO: ...
    @overload
    def version(self, **params: Unpack[LichessVersionTextResponseParams]) -> str: ...
    @overload
    def version(self, **params: Unpack[LichessVersionDefaultParams]) -> LichessVersionResponse: ...

OperationId = Literal[
    'lichess-cloud-eval',
    'lichess-enums',
    'lichess-puzzle',
    'lichess-puzzle-batch',
    'lichess-puzzle-daily',
    'lichess-puzzle-many',
    'lichess-puzzle-next',
    'lichess-puzzle-themes',
    'lichess-simuls',
    'lichess-tablebase',
    'lichess-version',
]

class CrawloraClient:
    lichess: LichessGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-cloud-eval'],
        params: LichessCloudEvalParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessCloudEvalResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-enums'],
        params: LichessEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle'],
        params: LichessPuzzleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle-batch'],
        params: LichessPuzzleBatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleBatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle-daily'],
        params: LichessPuzzleDailyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleDailyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle-many'],
        params: LichessPuzzleManyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleManyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle-next'],
        params: LichessPuzzleNextParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleNextResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-puzzle-themes'],
        params: LichessPuzzleThemesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleThemesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-simuls'],
        params: LichessSimulsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessSimulsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-tablebase'],
        params: LichessTablebaseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessTablebaseResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lichess-version'],
        params: LichessVersionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessVersionResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-cloud-eval'],
        params: LichessCloudEvalParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessCloudEvalResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-enums'],
        params: LichessEnumsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle'],
        params: LichessPuzzleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle-batch'],
        params: LichessPuzzleBatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleBatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle-daily'],
        params: LichessPuzzleDailyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleDailyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle-many'],
        params: LichessPuzzleManyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleManyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle-next'],
        params: LichessPuzzleNextParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleNextResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-puzzle-themes'],
        params: LichessPuzzleThemesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessPuzzleThemesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-simuls'],
        params: LichessSimulsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessSimulsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-tablebase'],
        params: LichessTablebaseParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessTablebaseResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lichess-version'],
        params: LichessVersionParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LichessVersionResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class LichessClient(CrawloraClient):
    def __enter__(self) -> LichessClient: ...
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalStreamParams]) -> BinaryIO: ...
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalTextResponseParams]) -> str: ...
    @overload
    def cloud_eval(self, **params: Unpack[LichessCloudEvalDefaultParams]) -> LichessCloudEvalResponse: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[LichessEnumsDefaultParams]) -> LichessEnumsResponse: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleTextResponseParams]) -> str: ...
    @overload
    def puzzle(self, **params: Unpack[LichessPuzzleDefaultParams]) -> LichessPuzzleResponse: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchTextResponseParams]) -> str: ...
    @overload
    def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchDefaultParams]) -> LichessPuzzleBatchResponse: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyTextResponseParams]) -> str: ...
    @overload
    def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyDefaultParams]) -> LichessPuzzleDailyResponse: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyTextResponseParams]) -> str: ...
    @overload
    def puzzle_many(self, **params: Unpack[LichessPuzzleManyDefaultParams]) -> LichessPuzzleManyResponse: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextTextResponseParams]) -> str: ...
    @overload
    def puzzle_next(self, **params: Unpack[LichessPuzzleNextDefaultParams]) -> LichessPuzzleNextResponse: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesStreamParams]) -> BinaryIO: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesTextResponseParams]) -> str: ...
    @overload
    def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesDefaultParams]) -> LichessPuzzleThemesResponse: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsStreamParams]) -> BinaryIO: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsTextResponseParams]) -> str: ...
    @overload
    def simuls(self, **params: Unpack[LichessSimulsDefaultParams]) -> LichessSimulsResponse: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseStreamParams]) -> BinaryIO: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseTextResponseParams]) -> str: ...
    @overload
    def tablebase(self, **params: Unpack[LichessTablebaseDefaultParams]) -> LichessTablebaseResponse: ...
    @overload
    def version(self, **params: Unpack[LichessVersionStreamParams]) -> BinaryIO: ...
    @overload
    def version(self, **params: Unpack[LichessVersionTextResponseParams]) -> str: ...
    @overload
    def version(self, **params: Unpack[LichessVersionDefaultParams]) -> LichessVersionResponse: ...

class AsyncLichessClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncLichessClient: ...
    lichess: _AsyncLichessGroup
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalStreamParams]) -> BinaryIO: ...
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalTextResponseParams]) -> str: ...
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalDefaultParams]) -> LichessCloudEvalResponse: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsDefaultParams]) -> LichessEnumsResponse: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleTextResponseParams]) -> str: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleDefaultParams]) -> LichessPuzzleResponse: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchTextResponseParams]) -> str: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchDefaultParams]) -> LichessPuzzleBatchResponse: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyTextResponseParams]) -> str: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyDefaultParams]) -> LichessPuzzleDailyResponse: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyTextResponseParams]) -> str: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyDefaultParams]) -> LichessPuzzleManyResponse: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextTextResponseParams]) -> str: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextDefaultParams]) -> LichessPuzzleNextResponse: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesTextResponseParams]) -> str: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesDefaultParams]) -> LichessPuzzleThemesResponse: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsStreamParams]) -> BinaryIO: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsTextResponseParams]) -> str: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsDefaultParams]) -> LichessSimulsResponse: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseStreamParams]) -> BinaryIO: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseTextResponseParams]) -> str: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseDefaultParams]) -> LichessTablebaseResponse: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionTextResponseParams]) -> str: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionDefaultParams]) -> LichessVersionResponse: ...

class _AsyncLichessGroup:
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalStreamParams]) -> BinaryIO: ...
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalTextResponseParams]) -> str: ...
    @overload
    async def cloud_eval(self, **params: Unpack[LichessCloudEvalDefaultParams]) -> LichessCloudEvalResponse: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[LichessEnumsDefaultParams]) -> LichessEnumsResponse: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleTextResponseParams]) -> str: ...
    @overload
    async def puzzle(self, **params: Unpack[LichessPuzzleDefaultParams]) -> LichessPuzzleResponse: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchTextResponseParams]) -> str: ...
    @overload
    async def puzzle_batch(self, **params: Unpack[LichessPuzzleBatchDefaultParams]) -> LichessPuzzleBatchResponse: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyTextResponseParams]) -> str: ...
    @overload
    async def puzzle_daily(self, **params: Unpack[LichessPuzzleDailyDefaultParams]) -> LichessPuzzleDailyResponse: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyTextResponseParams]) -> str: ...
    @overload
    async def puzzle_many(self, **params: Unpack[LichessPuzzleManyDefaultParams]) -> LichessPuzzleManyResponse: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextTextResponseParams]) -> str: ...
    @overload
    async def puzzle_next(self, **params: Unpack[LichessPuzzleNextDefaultParams]) -> LichessPuzzleNextResponse: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesStreamParams]) -> BinaryIO: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesTextResponseParams]) -> str: ...
    @overload
    async def puzzle_themes(self, **params: Unpack[LichessPuzzleThemesDefaultParams]) -> LichessPuzzleThemesResponse: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsStreamParams]) -> BinaryIO: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsTextResponseParams]) -> str: ...
    @overload
    async def simuls(self, **params: Unpack[LichessSimulsDefaultParams]) -> LichessSimulsResponse: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseStreamParams]) -> BinaryIO: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseTextResponseParams]) -> str: ...
    @overload
    async def tablebase(self, **params: Unpack[LichessTablebaseDefaultParams]) -> LichessTablebaseResponse: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionStreamParams]) -> BinaryIO: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionTextResponseParams]) -> str: ...
    @overload
    async def version(self, **params: Unpack[LichessVersionDefaultParams]) -> LichessVersionResponse: ...

LichessCloudEvalDefaultParams = TypedDict('LichessCloudEvalDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'fen': Required[str],
    'multiPv': NotRequired[int],
    'variant': NotRequired[Literal['standard', 'chess960', 'crazyhouse', 'antichess', 'atomic', 'horde', 'kingOfTheHill', 'racingKings', 'threeCheck', 'fromPosition']],
}, total=False)

LichessCloudEvalTextResponseParams = TypedDict('LichessCloudEvalTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'fen': Required[str],
    'multiPv': NotRequired[int],
    'variant': NotRequired[Literal['standard', 'chess960', 'crazyhouse', 'antichess', 'atomic', 'horde', 'kingOfTheHill', 'racingKings', 'threeCheck', 'fromPosition']],
}, total=False)

LichessCloudEvalStreamParams = TypedDict('LichessCloudEvalStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'fen': Required[str],
    'multiPv': NotRequired[int],
    'variant': NotRequired[Literal['standard', 'chess960', 'crazyhouse', 'antichess', 'atomic', 'horde', 'kingOfTheHill', 'racingKings', 'threeCheck', 'fromPosition']],
}, total=False)

LichessEnumsDefaultParams = TypedDict('LichessEnumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LichessEnumsTextResponseParams = TypedDict('LichessEnumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LichessEnumsStreamParams = TypedDict('LichessEnumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

LichessPuzzleDefaultParams = TypedDict('LichessPuzzleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

LichessPuzzleTextResponseParams = TypedDict('LichessPuzzleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

LichessPuzzleStreamParams = TypedDict('LichessPuzzleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

LichessPuzzleBatchDefaultParams = TypedDict('LichessPuzzleBatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'angle': Required[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'nb': NotRequired[int],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleBatchTextResponseParams = TypedDict('LichessPuzzleBatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'angle': Required[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'nb': NotRequired[int],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleBatchStreamParams = TypedDict('LichessPuzzleBatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'angle': Required[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'nb': NotRequired[int],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleDailyDefaultParams = TypedDict('LichessPuzzleDailyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LichessPuzzleDailyTextResponseParams = TypedDict('LichessPuzzleDailyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LichessPuzzleDailyStreamParams = TypedDict('LichessPuzzleDailyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

LichessPuzzleManyDefaultParams = TypedDict('LichessPuzzleManyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'ids': Required[str],
}, total=False)

LichessPuzzleManyTextResponseParams = TypedDict('LichessPuzzleManyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'ids': Required[str],
}, total=False)

LichessPuzzleManyStreamParams = TypedDict('LichessPuzzleManyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'ids': Required[str],
}, total=False)

LichessPuzzleNextDefaultParams = TypedDict('LichessPuzzleNextDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'angle': NotRequired[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleNextTextResponseParams = TypedDict('LichessPuzzleNextTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'angle': NotRequired[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleNextStreamParams = TypedDict('LichessPuzzleNextStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'angle': NotRequired[str],
    'difficulty': NotRequired[Literal['easiest', 'easier', 'normal', 'harder', 'hardest']],
    'color': NotRequired[Literal['white', 'black']],
}, total=False)

LichessPuzzleThemesDefaultParams = TypedDict('LichessPuzzleThemesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LichessPuzzleThemesTextResponseParams = TypedDict('LichessPuzzleThemesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LichessPuzzleThemesStreamParams = TypedDict('LichessPuzzleThemesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

LichessSimulsDefaultParams = TypedDict('LichessSimulsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LichessSimulsTextResponseParams = TypedDict('LichessSimulsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LichessSimulsStreamParams = TypedDict('LichessSimulsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

LichessTablebaseDefaultParams = TypedDict('LichessTablebaseDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'variant': Required[Literal['standard', 'atomic', 'antichess']],
    'fen': Required[str],
    'dtc': NotRequired[Literal['never', 'auxiliary', 'always']],
}, total=False)

LichessTablebaseTextResponseParams = TypedDict('LichessTablebaseTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'variant': Required[Literal['standard', 'atomic', 'antichess']],
    'fen': Required[str],
    'dtc': NotRequired[Literal['never', 'auxiliary', 'always']],
}, total=False)

LichessTablebaseStreamParams = TypedDict('LichessTablebaseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'variant': Required[Literal['standard', 'atomic', 'antichess']],
    'fen': Required[str],
    'dtc': NotRequired[Literal['never', 'auxiliary', 'always']],
}, total=False)

LichessVersionDefaultParams = TypedDict('LichessVersionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LichessVersionTextResponseParams = TypedDict('LichessVersionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LichessVersionStreamParams = TypedDict('LichessVersionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

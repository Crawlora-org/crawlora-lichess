<?php

declare(strict_types=1);

namespace Crawlora\Lichess;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'lichess';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 11;
    public const OPERATION_IDS = ["lichess-cloud-eval", "lichess-enums", "lichess-puzzle", "lichess-puzzle-batch", "lichess-puzzle-daily", "lichess-puzzle-many", "lichess-puzzle-next", "lichess-puzzle-themes", "lichess-simuls", "lichess-tablebase", "lichess-version"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"lichess-cloud-eval": {"bodyParam": null, "bodyRequired": false, "id": "lichess-cloud-eval", "method": "GET", "params": [{"description": "X-FEN chess position", "in": "query", "name": "fen", "required": true, "type": "string", "x-example": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}, {"description": "Number of principal variations requested; source default is 1", "in": "query", "name": "multiPv", "type": "integer"}, {"description": "Source chess variant; defaults to standard", "enum": ["standard", "chess960", "crazyhouse", "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck", "fromPosition"], "in": "query", "name": "variant", "type": "string"}], "path": "/lichess/cloud-eval", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "fen", "required": true, "type": "string"}, {"in": "query", "name": "multiPv", "type": "integer"}, {"enum": ["standard", "chess960", "crazyhouse", "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck", "fromPosition"], "in": "query", "name": "variant", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-enums": {"bodyParam": null, "bodyRequired": false, "id": "lichess-enums", "method": "GET", "params": [], "path": "/lichess/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-puzzle": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle", "method": "GET", "params": [{"description": "Lichess puzzle ID", "in": "query", "name": "id", "required": true, "type": "string"}], "path": "/lichess/puzzle", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-batch": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-batch", "method": "GET", "params": [{"description": "Open-ended upstream puzzle theme", "in": "query", "name": "angle", "required": true, "type": "string"}, {"description": "Optional source difficulty", "enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"description": "Number of puzzles, 1 through 50 (default 15)", "in": "query", "name": "nb", "type": "integer"}, {"description": "Optional side to move", "enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "path": "/lichess/puzzle/batch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "angle", "required": true, "type": "string"}, {"enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"in": "query", "name": "nb", "type": "integer"}, {"enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-daily": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-daily", "method": "GET", "params": [], "path": "/lichess/puzzle/daily", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-puzzle-many": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-many", "method": "GET", "params": [{"description": "Comma-separated list of 1 to 50 five-character Lichess puzzle IDs", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/lichess/puzzle/many", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-next": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-next", "method": "GET", "params": [{"description": "Optional upstream puzzle theme/angle; values are open-ended", "in": "query", "name": "angle", "type": "string"}, {"description": "Optional source difficulty", "enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"description": "Optional side to move", "enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "path": "/lichess/puzzle/next", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "angle", "type": "string"}, {"enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-themes": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-themes", "method": "GET", "params": [], "path": "/lichess/puzzle/themes", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-simuls": {"bodyParam": null, "bodyRequired": false, "id": "lichess-simuls", "method": "GET", "params": [], "path": "/lichess/simuls", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-tablebase": {"bodyParam": null, "bodyRequired": false, "id": "lichess-tablebase", "method": "GET", "params": [{"description": "Tablebase ruleset", "enum": ["standard", "atomic", "antichess"], "in": "query", "name": "variant", "required": true, "type": "string", "x-example": "standard"}, {"description": "Position in Forsyth-Edwards Notation", "in": "query", "name": "fen", "required": true, "type": "string", "x-example": "8/8/8/8/8/8/1K6/6k1 w - - 0 1"}, {"description": "Standard tablebase distance-to-conversion mode", "enum": ["never", "auxiliary", "always"], "in": "query", "name": "dtc", "type": "string"}], "path": "/lichess/tablebase", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["standard", "atomic", "antichess"], "in": "query", "name": "variant", "required": true, "type": "string"}, {"in": "query", "name": "fen", "required": true, "type": "string"}, {"enum": ["never", "auxiliary", "always"], "in": "query", "name": "dtc", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-version": {"bodyParam": null, "bodyRequired": false, "id": "lichess-version", "method": "GET", "params": [], "path": "/lichess/version", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-lichess-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function cloud_eval(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-cloud-eval", $params, $responseType);
    }
    public function enums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-enums", $params, $responseType);
    }
    public function puzzle(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle", $params, $responseType);
    }
    public function puzzle_batch(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle-batch", $params, $responseType);
    }
    public function puzzle_daily(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle-daily", $params, $responseType);
    }
    public function puzzle_many(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle-many", $params, $responseType);
    }
    public function puzzle_next(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle-next", $params, $responseType);
    }
    public function puzzle_themes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-puzzle-themes", $params, $responseType);
    }
    public function simuls(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-simuls", $params, $responseType);
    }
    public function tablebase(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-tablebase", $params, $responseType);
    }
    public function version(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lichess-version", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}

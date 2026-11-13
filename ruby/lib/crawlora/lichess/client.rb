require "json"
require "net/http"
require "uri"

module Crawlora
  module Lichess
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"lichess-cloud-eval": {"bodyParam": null, "bodyRequired": false, "id": "lichess-cloud-eval", "method": "GET", "params": [{"description": "X-FEN chess position", "in": "query", "name": "fen", "required": true, "type": "string", "x-example": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}, {"description": "Number of principal variations requested; source default is 1", "in": "query", "name": "multiPv", "type": "integer"}, {"description": "Source chess variant; defaults to standard", "enum": ["standard", "chess960", "crazyhouse", "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck", "fromPosition"], "in": "query", "name": "variant", "type": "string"}], "path": "/lichess/cloud-eval", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "fen", "required": true, "type": "string"}, {"in": "query", "name": "multiPv", "type": "integer"}, {"enum": ["standard", "chess960", "crazyhouse", "antichess", "atomic", "horde", "kingOfTheHill", "racingKings", "threeCheck", "fromPosition"], "in": "query", "name": "variant", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-enums": {"bodyParam": null, "bodyRequired": false, "id": "lichess-enums", "method": "GET", "params": [], "path": "/lichess/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-puzzle": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle", "method": "GET", "params": [{"description": "Lichess puzzle ID", "in": "query", "name": "id", "required": true, "type": "string"}], "path": "/lichess/puzzle", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-batch": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-batch", "method": "GET", "params": [{"description": "Open-ended upstream puzzle theme", "in": "query", "name": "angle", "required": true, "type": "string"}, {"description": "Optional source difficulty", "enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"description": "Number of puzzles, 1 through 50 (default 15)", "in": "query", "name": "nb", "type": "integer"}, {"description": "Optional side to move", "enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "path": "/lichess/puzzle/batch", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "angle", "required": true, "type": "string"}, {"enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"in": "query", "name": "nb", "type": "integer"}, {"enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-daily": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-daily", "method": "GET", "params": [], "path": "/lichess/puzzle/daily", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-puzzle-many": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-many", "method": "GET", "params": [{"description": "Comma-separated list of 1 to 50 five-character Lichess puzzle IDs", "in": "query", "name": "ids", "required": true, "type": "string"}], "path": "/lichess/puzzle/many", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "ids", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-next": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-next", "method": "GET", "params": [{"description": "Optional upstream puzzle theme/angle; values are open-ended", "in": "query", "name": "angle", "type": "string"}, {"description": "Optional source difficulty", "enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"description": "Optional side to move", "enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "path": "/lichess/puzzle/next", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "angle", "type": "string"}, {"enum": ["easiest", "easier", "normal", "harder", "hardest"], "in": "query", "name": "difficulty", "type": "string"}, {"enum": ["white", "black"], "in": "query", "name": "color", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-puzzle-themes": {"bodyParam": null, "bodyRequired": false, "id": "lichess-puzzle-themes", "method": "GET", "params": [], "path": "/lichess/puzzle/themes", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-simuls": {"bodyParam": null, "bodyRequired": false, "id": "lichess-simuls", "method": "GET", "params": [], "path": "/lichess/simuls", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "lichess-tablebase": {"bodyParam": null, "bodyRequired": false, "id": "lichess-tablebase", "method": "GET", "params": [{"description": "Tablebase ruleset", "enum": ["standard", "atomic", "antichess"], "in": "query", "name": "variant", "required": true, "type": "string", "x-example": "standard"}, {"description": "Position in Forsyth-Edwards Notation", "in": "query", "name": "fen", "required": true, "type": "string", "x-example": "8/8/8/8/8/8/1K6/6k1 w - - 0 1"}, {"description": "Standard tablebase distance-to-conversion mode", "enum": ["never", "auxiliary", "always"], "in": "query", "name": "dtc", "type": "string"}], "path": "/lichess/tablebase", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["standard", "atomic", "antichess"], "in": "query", "name": "variant", "required": true, "type": "string"}, {"in": "query", "name": "fen", "required": true, "type": "string"}, {"enum": ["never", "auxiliary", "always"], "in": "query", "name": "dtc", "type": "string"}], "security": ["ApiKeyAuth"]}, "lichess-version": {"bodyParam": null, "bodyRequired": false, "id": "lichess-version", "method": "GET", "params": [], "path": "/lichess/version", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["lichess-cloud-eval", "lichess-enums", "lichess-puzzle", "lichess-puzzle-batch", "lichess-puzzle-daily", "lichess-puzzle-many", "lichess-puzzle-next", "lichess-puzzle-themes", "lichess-simuls", "lichess-tablebase", "lichess-version"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-lichess-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('cloud_eval') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-cloud-eval', params, response_type: response_type)
      end
      define_method('enums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-enums', params, response_type: response_type)
      end
      define_method('puzzle') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle', params, response_type: response_type)
      end
      define_method('puzzle_batch') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle-batch', params, response_type: response_type)
      end
      define_method('puzzle_daily') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle-daily', params, response_type: response_type)
      end
      define_method('puzzle_many') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle-many', params, response_type: response_type)
      end
      define_method('puzzle_next') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle-next', params, response_type: response_type)
      end
      define_method('puzzle_themes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-puzzle-themes', params, response_type: response_type)
      end
      define_method('simuls') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-simuls', params, response_type: response_type)
      end
      define_method('tablebase') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-tablebase', params, response_type: response_type)
      end
      define_method('version') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lichess-version', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end

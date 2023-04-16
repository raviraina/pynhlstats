from request_builder import RequestBuilder


class NhlApiRequestProcessor:
    def __init__(self):
        self.rb = RequestBuilder("https://statsapi.web.nhl.com")

    def request(self, req: str, name: str, refresh: bool) -> dict:
        return self.rb.make_and_cache_request(req, name, refresh)

import requests
import json
import os


class RequestBuilder:
    def __init__(self, base_api, cache_dir="../data"):
        self.CACHE_DIR = cache_dir
        self.BASE_API = base_api
        self.PWD = os.getcwd()

    def make_and_cache_request(
        self, endpoint: str, cache_name: str, overwrite: bool = False
    ) -> dict:

        cache = f"{self.PWD}/{self.CACHE_DIR}/{cache_name}.json"

        if os.path.isfile(cache) and not overwrite:
            print(f"Reading from cache {cache}")
            with open(cache, "r") as f:
                return json.load(f)

        else:
            print(f"Saving and reading from response to {cache}")

            try:
                req = f"{self.BASE_API}{endpoint}"
                res = requests.get(req)
            except:
                raise Exception("Invalid request")

            try:
                with open(cache, "w") as f:
                    json.dump(res.json(), f, ensure_ascii=False, indent=4)
            except:
                raise Exception("Unable to write to cache")

            return res.json()

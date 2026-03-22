import requests

class BaseAPI:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://api.thedogapi.com/v1"
        self.session.headers.update({
            "Content-Type": "application/json",
            "x-api-key": "live_NfqDwTPSNBeMeQBuw1rEPE25nspszUzfvYFb8PDnsvJU3uiKeVOtc9hOdXIDPIwC"
        })

    def _request(self, method, endpoint, **kwargs):
        kwargs.setdefault('timeout', 10)
        url = self.base_url + endpoint
        return self.session.request(method, url, **kwargs)

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)
import requests


class APIConnection:
    def __init__(self, url) -> None:
        self._url = url

    def get(self, endpoint) -> dict[str, str]:
        full_url = f'{self._url}{endpoint}'
        return requests.get(full_url).json()

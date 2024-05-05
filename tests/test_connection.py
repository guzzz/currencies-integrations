from pytest import raises
from requests.exceptions import ConnectionError, MissingSchema

from currencies_integrations.connection import APIConnection


def test_cant_connect_with_api_wrong_url():
    api = APIConnection('test')
    error_message = 'Error while trying to connect to third party api. Probably and invalid URL.'

    with raises(MissingSchema, match=(error_message)):
        api.get('/endpoint')


def test_cant_connect_with_api():
    api = APIConnection('https://example.invalid')
    error_message = 'Error while trying to connect to third party api.'

    with raises(ConnectionError, match=(error_message)):
        response = api.get('/endpoint')
        response.raise_for_status()

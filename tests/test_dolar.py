from currencies_integrations.dolar import comercial


def test_comercial_should_return_dict():
    response = comercial()
    assert type(response) == dict

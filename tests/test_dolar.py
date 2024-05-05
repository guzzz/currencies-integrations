from currencies_integrations.dolar import dolar_comercial, dolar_turismo


def test_dolar_comercial_should_return_dict():
    response = dolar_comercial()
    assert type(response) == dict


def test_dolar_turismo_should_return_dict():
    response = dolar_turismo()
    assert type(response) == dict

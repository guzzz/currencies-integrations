from .connection import APIConnection


def comercial() -> dict[str, str]:
    """
    Retorna a cotação do dólar comercial em BRL.

    Returns:
        Um dicionário com o valor da cotação. Ex.: {'value': 5.00000}

    Raises:
        ConnectionError: Caso não seja possível conectar com a API que nos daria o resultado.
        MissingSchema: Caso a url da API terceira esteja equivocada.

    Examples:
        >>> type(comercial())
        <class 'dict'>
    """
    api = APIConnection('https://economia.awesomeapi.com.br/json/last')
    response = api.get('/USD-BRL')
    data = response['USDBRL']
    high = float(data['high'])
    low = float(data['low'])
    average = (high + low) / 2
    return {'value': average}

from typer.testing import CliRunner

from currencies_integrations.cli import app

runner = CliRunner()


def test_dolar_comercial_should_return_0_to_stdout():
    result = runner.invoke(app, ['dolar-comercial'])
    assert result.exit_code == 0


def test_dolar_turismo_should_return_0_to_stdout():
    result = runner.invoke(app, ['dolar-turismo'])
    assert result.exit_code == 0

from typer.testing import CliRunner

from run import app


runner = CliRunner()


def test_app_no_args():
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Simple budget tracker CLI" in result.stdout
    assert "--help" in result.stdout
    assert "add" in result.stdout


def test_app_add_record():
    result = runner.invoke(app, args=["add"])
    assert result.exit_code == 0


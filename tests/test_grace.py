from click.testing import CliRunner

import grace.main


def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(grace.main.main, ["--version"])
    assert result.exit_code == 0
    assert grace.__version__ in result.output.split()

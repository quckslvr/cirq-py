from click.testing import CliRunner
from cirq.commands.cirq import cirq

runner = CliRunner()


def test_cirq__root_command__without_flag():
    result = runner.invoke(cirq)
    assert result.exit_code == 0


def test_cirq__root_command__with_flag():
    result = runner.invoke(cirq, ["--verbose"])
    assert result.exit_code == 0
    assert "Verbose" and "on" in result.output


def test_cirq__repo_class__function__retrieve_repo():
    result = runner.invoke(cirq)
    assert result.exit_code == 0



if __name__ == "__main__":
    test_cirq__root_command__without_flag()
    test_cirq__root_command__with_flag()

    test_cirq__repo_class__function__retrieve_repo()

from click.testing import CliRunner
from cirq.commands.cirq import cirq

runner = CliRunner()


def test_generate_command_with_flag():
    result = runner.invoke(cirq, ['generate', 'Max', '--flag'])
    assert result.exit_code == 0
    assert 'Max' and 'Flag is set' in result.output


# def test_generate_command_without_flag():
#     result = runner.invoke(cirq, ['generate', 'name_value'])
#     assert result.exit_code == 0
#     assert 'root_arg_value name_value' in result.output
#     assert 'Flag is not set' in result.output


if __name__ == '__main__':
    test_generate_command_with_flag()
    # test_generate_command_without_flag()

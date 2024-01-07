import click

from cirq.commands.cirq import cirq


@cirq.command()
def init():
    """Implementation for the init subcommand."""
    # todo verify if there's a .git folder and .cirq file (look at parent directory)
    # todo make conditions based on the above
    # todo init project structure
    # todo invoke generate command with template
    click.echo("Init command executed.")

import click

from cirq.commands.cirq import cirq


@cirq.command()
def doctor():
    """Implementation for the info subcommand."""
    click.echo('Doctor command executed.')

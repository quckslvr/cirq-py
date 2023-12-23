import click

from cirq.commands.cirq import cirq


@cirq.command()
def init():
    """Implementation for the init subcommand."""
    click.echo('Init command executed.')

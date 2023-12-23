import click

from cirq.commands.cirq import cirq


@cirq.command()
def info():
    """Implementation for the info subcommand."""
    click.echo('Info command executed.')

import click

from cirq.commands.cirq import cirq


@cirq.command()
def version():
    """Implementation for the version subcommand."""
    click.echo("Version command executed.")

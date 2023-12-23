import click

from cirq.commands.cirq import cirq


@cirq.command()
@click.argument('name')
@click.option('--flag', '-f', default=False, is_flag=True)
def generate(name, flag):
    message = f'{name}'
    click.echo(message)
    if flag:
        click.echo('Flag is set')
    else:
        click.echo('Flag is not set')
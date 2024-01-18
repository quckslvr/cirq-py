import os

import click

from cirq.commands.cirq import cirq
from cirq.commands.generate import generate


@cirq.command()
@click.argument("name", type=click.STRING, nargs=1, required=False)
@click.pass_context
def new(ctx, name):
    """Initialize a new project."""
    cirq_context = ctx.obj
    cirq_context.repo_name = name

    if cirq_context.repo_path:
        click.echo("Repo already exists.")
        return

    # todo init project structure
    if name is None:
        cwd_name = os.path.basename(cirq_context.current_dir)
        default_project_name = f"{cwd_name}-project"
        name = click.prompt("Project name", default=default_project_name)
        cirq_context.repo_name = name

    click.echo(f"Creating new project: {name}")
    cirq_context.repo_path = cirq_context.current_dir + "/" + name

    os.makedirs(name, exist_ok=False)

    os.system(f"git init {name}")
    open(os.path.join(name, ".cirq"), "w").close()

    # todo invoke generate command with template
    cirq_context.new_project = True
    ctx.invoke(generate, name="home")

    click.echo("Init command executed.")

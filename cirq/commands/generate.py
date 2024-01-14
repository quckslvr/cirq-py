import click
import os

from cirq.commands.cirq import cirq


def generate_file(directory, filename, content):
    file_path = os.path.join(directory, filename + ".py")
    with open(file_path, "w") as file:
        # if False:
        #     print("Would generate file: {}".format(file_path))
        #     return
        file.write(content)
        click.echo("Generated file: {}".format(file_path))


# Controller
controller_content = """\
from app.views.{view_module} import {view_function}

def {controller_function}():
    return {view_function}()
"""


@cirq.command()
@click.argument("name", required=True)
@click.pass_obj
def generate(ctx_obj, name=str) -> None:
    """Generate the controller, model, and view files for a new component."""

    # Project root directory
    # todo find a way to have a state project file to found the workspace
    project_root = ctx_obj.repo_path

    # Directories for controllers, models, routes, and views

    controller_dir = os.path.join(project_root, "app", "controllers")
    model_dir = os.path.join(project_root, "app", "models")
    route_dir = os.path.join(project_root, "config")
    view_dir = os.path.join(project_root, "app", "views")

    # Create directories if they don't exist
    for directory in [controller_dir, model_dir, route_dir, view_dir]:
        if ctx_obj.dryrun:
            click.echo("Would create directory: {}".format(directory))
            return
        os.makedirs(directory, exist_ok=True)

    generate_file(controller_dir, f"{name}_controller", controller_content)

    # Model
    model_content = """\
    class ExampleModel:
        def __init__(self, name):
            self.name = name
    """

    generate_file(model_dir, f"{name}_model", model_content)

    # Route
    route_content = """\
    from app.controllers.example_controller import {controller_function}

    def setup_routes(app):
        app.add_url_rule('/', 'example', {controller_function})
    """

    generate_file(route_dir, "route.py", route_content)

    # Views
    view_content = """\
    def {view_function}():
        return "Hello from the {view_function} view!"
    """

    generate_file(view_dir, f"{name}_view", view_content)

    click.echo("Files generated successfully.")

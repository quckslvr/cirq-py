import click
import os

from cirq.commands.cirq import cirq

# Server
app_content = """\
from flask import Flask
from config.route import setup_routes

{name} = Flask(__name__)
setup_routes({name})

if __name__ == '__main__':
    {name}.run()
"""

# Controller
controller_content = """\
from app.views.{name}_view import {name}_view


class {cap_name}Controller:
    def index(self):
        # Your GET logic here
        return {name}_view()

    def post_index(self):
        # Your POST logic here
        return "This is a POST request."
"""

# Model
model_content = """\
class {cap_name}Model:
    def __init__(self, name):
        self.name = name
"""

# Views
view_content = """\
def {name}_view() -> str:
    return "Hello from the {name} view!"
"""

# Route
route_content = """\
from app.controllers.{name}_controller import {cap_name}Controller


def setup_routes(app) -> None:
    app.add_url_rule('{endpoint}', '{name}', {cap_name}Controller().index)
"""


def generate_file(directory, filename, content):
    file_path = os.path.join(directory, filename + ".py")
    with open(file_path, "w") as file:
        # if False:
        #     print("Would generate file: {}".format(file_path))
        #     return
        file.write(content)
        click.echo("Generated file: {}".format(file_path))


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

    if ctx_obj.new_project:
        # If this is a new project we need to generate the app.py file

        generate_file(project_root, "main", app_content.format(name=ctx_obj.repo_name))

        # We also need to generate the __init__.py file for the app directory
        generate_file(project_root, "__init__", "")

    # Create directories if they don't exist
    for directory in [controller_dir, model_dir, route_dir, view_dir]:
        if ctx_obj.dryrun:
            click.echo("Would create directory: {}".format(directory))
            return

        os.makedirs(directory, exist_ok=True)

    # todo make this more beautiful
    generate_file(model_dir, f"{name}_model", model_content.format(cap_name=name.capitalize(), name=name))
    generate_file(view_dir, f"{name}_view", view_content.format(name=name))

    generate_file(controller_dir, f"{name}_controller", controller_content.format(
        cap_name=name.capitalize(),
        name=name))

    generate_file(route_dir, "route", route_content.format(
        name=name,
        cap_name=name.capitalize(),
        endpoint="/" if ctx_obj.new_project else "/" + str(name)))

    click.echo("Files generated successfully.")

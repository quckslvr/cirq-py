import json
import os

import click

SEPERATOR = f"\n{'-' * 40}"


class Cirq(object):
    def __init__(self, dryrun=False, verbose=False):
        self.dryrun: bool = dryrun
        self.verbose: bool = verbose
        self.new_project: bool = False

        self.current_dir: str = os.getcwd()
        self.repo_path: str = self.retrieve_repo()
        self.repo_found: bool = bool(self.repo_path)
        self.repo_name: str = os.path.basename(self.repo_path)

    def retrieve_repo(self) -> str:
        return self._find_cirq_file()

    def _find_cirq_file(self) -> str:
        """
        Search for a .cirq file in the current directory and its parent directories.

        Returns:
            str: The path to the found .cirq file, or False if not found.
        """
        current_dir: str = self.current_dir

        while True:
            cirq_file_path = os.path.join(current_dir, '.cirq')
            if os.path.isfile(cirq_file_path):
                return current_dir

            # Move up one directory
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                # Reached the root directory, stop searching
                break

            current_dir = parent_dir

        return ""


@click.group(invoke_without_command=True)
@click.option(
    "--dryrun", "-d", is_flag=True, default=False, help="Enables Dry run mode.",
)
@click.option(
    "--verbose", "-v",
    envvar="CIRQ_VERBOSE",
    is_flag=True,
    default=False,
    help="Enables verbose mode.",
)
@click.pass_context
def cirq(ctx, dryrun, verbose):
    """Run the CLI."""
    ctx.obj = Cirq(dryrun=dryrun, verbose=verbose)

    if ctx.invoked_subcommand is None:
        if ctx.obj.verbose:
            click.echo("Verbose mode is on.")
            click.echo(SEPERATOR)
            click.echo(f"Invoked subcommand: {ctx.invoked_subcommand}")
            click.echo(f"Context object: {json.dumps(ctx.obj.__dict__)}")  # todo remove this line
            click.echo(SEPERATOR)
        click.echo(cirq.get_help(ctx))

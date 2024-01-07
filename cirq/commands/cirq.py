import os

import click


class Repo(object):
    def __init__(self, dryrun=False, verbose=False):
        self.current_dir = os.getcwd()
        self.repo_path = self.retrieve_repo()

        self.dryrun = dryrun
        self.verbose = verbose

    def retrieve_repo(self) -> str:
        return self._find_cirq_file()

    def _find_cirq_file(self) -> str | bool:
        """
        Search for a .cirq file in the current directory and its parent directories.

        Returns:
            str: The path to the found .cirq file, or False if not found.
        """
        current_dir = self.current_dir

        while True:
            cirq_file_path = os.path.join(current_dir, '.cirq')
            if os.path.isfile(cirq_file_path):
                print(f"Found .cirq file at: {cirq_file_path}")
                return current_dir

            # Move up one directory
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:
                # Reached the root directory, stop searching
                break

            current_dir = parent_dir
        print("No .cirq file found.")
        return False


@click.group(invoke_without_command=True)
@click.option(
    "--dryrun", "-d", default=False, is_flag=True, help="Enables Dry run mode."
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
    ctx.obj = Repo(dryrun=dryrun, verbose=verbose)

    if ctx.invoked_subcommand is None and ctx.obj.verbose:

        #  todo implement a proper verbose mode with logging
        click.echo("Verbose mode is on.")
        click.echo("Invoked subcommand: {}".format(ctx.invoked_subcommand))
        click.echo(ctx.obj.__dict__)   # todo remove this line

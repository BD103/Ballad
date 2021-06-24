import click

from . import core, utils


@click.group()
def cli():
  """Install Poetry Project without Poetry"""
  pass


@cli.command()
@click.option("-d/-p", "--development/--production", default=True)
@click.option("-l", "--lockfile", default="poetry.lock")
@click.option("-q", "--quiet", is_flag=True)
def install(development: bool, lockfile: str, quiet: bool):
  """Install dependencies from lockfile using PIP"""
  ballad = core.Ballad()
  ballad.lockfile_name = lockfile

  if not development:
    ballad.environment = "production"

  ballad.install(quiet)


@cli.command()
@click.option("-l", "--lock", default="poetry.lock")
@click.option("-o", "--output", default="poetry.json")
def convert_lock(lock: str, output: str):
  """Reads lockfile, convert it to JSON, then outputs to file"""
  utils.convert_lock(lock, output)


if __name__ == "__main__":
  cli()

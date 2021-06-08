import click

from . import loader
from .tests import convert_lock as _convert_lock


@click.group()
def cli():
  """Install Poetry Project without Poetry"""
  pass


@cli.command()
@click.option("-d/-nd", "--dev-dep/--no-dev-dep", default=True)
@click.option("-D/-nD", "--debug/--no-debug", default=False)
def install(dev_dep: bool, debug: bool):
  """Install Dependencies from Lock File"""
  if dev_dep:
    loader.load_all(debug=debug)
  else:
    loader.load_production(debug=debug)


@cli.command()
@click.option("-l", "--lock", default="poetry.lock")
@click.option("-o", "--output", default="poetry.json")
def convert_lock(lock, output):
  """Exports poetry.lock to poetry.json"""
  _convert_lock(lock=lock, output=output)


if __name__ == "__main__":
  cli()

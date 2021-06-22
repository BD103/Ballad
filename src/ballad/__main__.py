import click

from . import utils as _utils


@click.group()
def cli():
  """Install Poetry Project without Poetry"""
  pass


@cli.command()
@click.option("-l", "--lock", default="poetry.lock")
@click.option("-o", "--output", default="poetry.json")
def convert_lock(lock: str = "poetry.lock", output: str = "poetry.json"):
  _utils.convert_lock(lock, output)


if __name__ == "__main__":
  cli()

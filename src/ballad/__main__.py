import click

from . import loader


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


if __name__ == "__main__":
  cli()

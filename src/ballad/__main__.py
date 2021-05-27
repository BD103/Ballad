import click


@click.group()
def cli():
  """Install Poetry Project without Poetry"""
  pass


@cli.command()
def install():
  """Install Dependencies"""
  pass


if __name__ == "__main__":
  cli()

import click


@click.group()
def cli():
  """Install Poetry Project without Poetry"""
  pass


if __name__ == "__main__":
  cli()

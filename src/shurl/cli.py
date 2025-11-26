import rich_click as click


@click.group()
def cli():
    """URL shortener."""


@cli.command()
@click.option('--key-length', type=int)
def add_entry(key_length: int):
    """Add new project entry."""

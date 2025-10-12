import rich_click as click

from . import core


@click.group()
def cli():
    """"""

@cli.command()
@click.argument('length', type=int)
def add(length: int):
    """
    Generate short key for url and add it to mappings file.

    :param length:
    :return:
    """
    key = core.new_key(length)
    click.echo(key)

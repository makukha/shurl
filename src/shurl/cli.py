from enum import StrEnum, auto

import rich
import rich_click as click
from rich.pretty import Pretty

from .workspace import Project, Workspace, json_converter


class OutputFormat(StrEnum):
    JSON = auto()
    TEXT = auto()


@click.group()
def cli() -> None:
    """URL shortener."""


@cli.group()
def project() -> None:
    """Manage shurl project."""


@cli.group()
def workspace() -> None:
    """Manage shurl workspace."""


# project


@project.command(name='cat')
@click.option(
    '--format',
    '-t',
    type=click.Choice(OutputFormat, case_sensitive=False),
    default=OutputFormat.TEXT,
    help='Output format.',
)
@click.argument(
    'file',
    required=True,
    type=click.Path(exists=True, readable=True, dir_okay=False),
)
def project_cat(format: OutputFormat, file: click.Path) -> None:
    """Pretty print project file."""
    proj = Project.load_toml(str(file))
    match format:
        case OutputFormat.JSON:
            print(json_converter.dumps(proj, indent=2))
        case OutputFormat.TEXT:
            rich.print(Pretty(proj, indent_size=2, indent_guides=True))
        case _:
            raise ValueError(f'Unsupported format: {format}')


# workspace


@workspace.command(name='cat')
@click.option(
    '--format',
    '-t',
    type=click.Choice(OutputFormat, case_sensitive=False),
    default=OutputFormat.TEXT,
    help='Output format.',
)
@click.argument(
    'file',
    type=click.Path(exists=True, readable=True, dir_okay=False),
    default='workspace.toml',
)
def workspace_cat(format: OutputFormat, file: click.Path) -> None:
    """Pretty print workspace file."""
    ws = Workspace.load_toml(str(file))
    match format:
        case OutputFormat.JSON:
            print(json_converter.dumps(ws, indent=2))
        case OutputFormat.TEXT:
            rich.print(Pretty(ws, indent_size=2, indent_guides=True))
        case _:
            raise ValueError(f'Unsupported format: {format}')


@workspace.command()
@click.argument(
    'file',
    type=click.Path(exists=True, readable=True, dir_okay=False),
    default='workspace.toml',
)
def sync(file: click.Path) -> None:
    """Sync workspace to all destinations."""
    ws = Workspace.load_toml(str(file))
    ws.sync()

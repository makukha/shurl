from bz2 import BZ2File
from dataclasses import dataclass
from datetime import UTC
from pathlib import Path
from tarfile import TarFile
from typing import Any, Self

import cattrs.preconf.json
import cattrs.preconf.tomlkit
import date62

from .utils import absolute_path, provide_clean_directory, rmpath

json_converter = cattrs.preconf.json.make_converter()
toml_converter = cattrs.preconf.tomlkit.make_converter()


@dataclass
class Entry:
    key: str
    description: str
    redirect_url: str | None = None
    permanent: bool = False


@dataclass(kw_only=True)
class Project:
    path: Path | None = None
    entries: list[Entry]

    @classmethod
    def from_dict(cls, data: list[dict[str, Any]]) -> Self:
        return cattrs.structure(data, cls)

    @classmethod
    def load_toml(cls, path: str | Path) -> Self:
        p = Path(path).absolute()
        obj = toml_converter.loads(p.read_text(), cls)
        obj.path = p
        return obj

    def dump_nginx_config(self, path: Path) -> None:
        with path.open('w') as f:
            for entry in self.entries:
                result = (
                    f'{"301" if entry.permanent else "302"} {entry.redirect_url}'
                    if entry.redirect_url
                    else '404'
                )
                f.write(
                    f'location /{entry.key} {{ return {result}; }}  # {entry.description}\n'
                )


@dataclass(kw_only=True)
class Workspace:
    path: Path | None = None
    projects_dir: str
    backups_dir: str
    nginx_configs_dir: str

    @classmethod
    def load_toml(cls, path: str | Path) -> Self:
        p = Path(path).absolute()
        obj = toml_converter.loads(p.read_text(), cls)
        obj.path = p
        return obj

    def abs(self, path: str | Path) -> Path:
        return absolute_path(path, anchor=self.path)

    def sync(self) -> None:
        bak = self.backup()
        try:
            self.dump_nginx_configs()
        except Exception:
            self.restore(bak)
            raise

    def dump_nginx_configs(self) -> None:
        provide_clean_directory(self.abs(self.nginx_configs_dir))
        for p in self.abs(self.projects_dir).glob('*.toml'):
            n = self.abs(self.nginx_configs_dir) / p.with_suffix('.conf').name
            Project.load_toml(p).dump_nginx_config(n)

    def backup(self) -> Path:
        backups_dir = self.abs(self.backups_dir)
        backups_dir.mkdir(parents=True, exist_ok=True)
        path = backups_dir / f'{date62.now(tz=UTC)}.tar.bz2'
        with BZ2File(path, 'wb', compresslevel=9) as f:
            with TarFile(fileobj=f, mode='w') as bak:
                for src, tgt in (
                    (self.path, 'workspace.toml'),
                    (self.projects_dir, 'projects'),
                    (self.nginx_configs_dir, 'nginx/projects'),
                ):
                    if src and self.abs(src).exists():
                        bak.add(self.abs(src), arcname=tgt)
        return path

    def restore(self, path: str | Path) -> None:
        with TarFile(path, 'r') as bak:
            for src, tgt in (
                # workspace.toml is not restored
                ('projects', self.projects_dir),
                ('nginx/projects', self.nginx_configs_dir),
            ):
                if bak.getmember(src) is not None:
                    if tgt and self.abs(tgt).exists():
                        rmpath(tgt)
                    bak.extract(src, path=tgt)

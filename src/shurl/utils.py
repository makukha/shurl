from pathlib import Path
from shutil import rmtree


def absolute_path(path: str | Path, anchor: str | Path | None) -> Path:
    path = Path(path)
    return (
        path
        if anchor is None or path.is_absolute()
        else (Path(anchor).parent / path).absolute()
    )


def provide_clean_directory(path: str | Path) -> None:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    for item in p.iterdir():
        rmpath(item)


def rmpath(path: str | Path) -> None:
    p = Path(path)
    if p.exists():
        if p.is_dir():
            rmtree(p)
        else:
            p.unlink()

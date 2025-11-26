from dataclasses import dataclass


@dataclass
class Entry:
    key: str
    title: str
    redirect_url: str


@dataclass
class Project:
    endpoints: list[Entry]
    path: str

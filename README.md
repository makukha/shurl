# shurl

> Short URL service.


<!-- docsub: begin -->
<!-- docsub: include docs/badges.md -->
[![license](https://img.shields.io/github/license/makukha/shurl.svg)](https://github.com/makukha/shurl/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/shurl.svg#v0.0.0)](https://pypi.org/project/shurl)
[![python versions](https://img.shields.io/pypi/pyversions/shurl.svg)](https://pypi.org/project/shurl)
[![tests](https://raw.githubusercontent.com/makukha/shurl/v0.0.0/docs/img/badge/tests.svg)](https://github.com/makukha/shurl)
[![coverage](https://raw.githubusercontent.com/makukha/shurl/v0.0.0/docs/img/badge/coverage.svg)](https://github.com/makukha/shurl)
[![tested with multipython](https://img.shields.io/badge/tested_with-multipython-x)](https://github.com/makukha/multipython)
[![uses docsub](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/makukha/docsub/refs/heads/main/docs/badge/v1.json)](https://github.com/makukha/docsub)
[![mypy](https://img.shields.io/badge/type_checked-mypy-%231674b1)](http://mypy.readthedocs.io)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/ruff)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![openssf best practices](https://www.bestpractices.dev/projects/10749/badge)](https://www.bestpractices.dev/projects/)
<!-- docsub: end -->


# Features

<!-- docsub: begin -->
<!-- docsub: include docs/features.md -->
- Minimalistic and fast
- Text-based URL mappings managed by Git
- Persist access logs in S3 bucket
- Use as library or deploy as FastAPI service
- Case-insensitive urls
<!-- docsub: end -->


# Installation

```shell
$ pip install shurl
```


# Usage

<!-- docsub: begin #usage.md -->
<!-- docsub: include docs/usage.md -->
<!-- docsub: begin -->
<!-- docsub: x toc tests/test_usage.py 'Usage.*' -->
* [First use case](#first-use-case)
<!-- docsub: end -->

```pycon
>>> from shurl import *  # todo
```

<!-- docsub: begin -->
<!-- docsub: x cases tests/test_usage.py 'Usage.*' -->
## First use case

```pycon
>>> from shurl import __version__
```

<!-- docsub: end -->
<!-- docsub: end #usage.md -->


# CLI Reference

<!-- docsub: begin #cli.md -->
<!-- docsub: include docs/cli.md -->
<!-- docsub: begin -->
<!-- docsub: help shurl -->
<!-- docsub: lines after 2 upto -1 -->
<!-- docsub: strip -->
```shell
$ shurl --help
Usage: shurl [OPTIONS] COMMAND [ARGS]...

URL shortener.

╭─ Options ──────────────────────────────────────────────────────────╮
│ --help  Show this message and exit.                                │
╰────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────╮
│ project              Manage shurl project.                         │
│ workspace            Manage shurl workspace.                       │
╰────────────────────────────────────────────────────────────────────╯
```
<!-- docsub: end -->
<!-- docsub: end #cli.md -->


# Contributing

Pull requests, feature requests, and bug reports are welcome!

* [Contribution guidelines](https://github.com/makukha/shurl/blob/main/.github/CONTRIBUTING.md)


# Authors

* Michael Makukha


# See also

* [Documentation](https://github.com/makukha/shurl#readme)
* [Issues](https://github.com/makukha/shurl/issues)
* [Changelog](https://github.com/makukha/shurl/blob/main/CHANGELOG.md)
* [Security Policy](https://github.com/makukha/shurl/blob/main/.github/SECURITY.md)
* [Contribution Guidelines](https://github.com/makukha/shurl/blob/main/.github/CONTRIBUTING.md)
* [Code of Conduct](https://github.com/makukha/shurl/blob/main/.github/CODE_OF_CONDUCT.md)
* [License](https://github.com/makukha/shurl/blob/main/LICENSE)

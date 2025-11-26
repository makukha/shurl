FROM ghcr.io/astral-sh/uv:python3.14-trixie AS builder
COPY pyproject.toml uv.lock /
RUN uv venv
COPY README.md /
COPY src /src
RUN uv build .

FROM docker.io/nginx:mainline-trixie AS shurl-nginx-cli
COPY --from=ghcr.io/astral-sh/uv:0.9.12 /uv /uvx /bin/

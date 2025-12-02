ARG PYTHON_VERSION=3.13
ARG UV_VERSION=0.9.13

FROM ghcr.io/astral-sh/uv:${UV_VERSION}-python${PYTHON_VERSION}-trixie AS builder
ARG PYTHON_VERSION
ARG UV_VERSION
WORKDIR /build
COPY pyproject.toml uv.lock /build/
RUN uv venv
COPY README.md /build/
COPY src /build/src
RUN uv build .

FROM docker.io/nginx:mainline-trixie AS nginx
ARG PYTHON_VERSION
ARG UV_VERSION
COPY --from=ghcr.io/astral-sh/uv:${UV_VERSION} /uv /uvx /bin/
RUN <<-EOS
    useradd -m -u 1000 -d /opt/shurl shurl
    mkdir -p /var/lib/shurl
    chown -R shurl:shurl /opt/shurl /var/lib/shurl
EOS
COPY --from=builder /build/dist/shurl-*.whl /opt/shurl/dist/
RUN su shurl -c 'uv tool install /opt/shurl/dist/shurl-*.whl'
COPY ./tests/examples/nginx/nginx.conf /etc/nginx/conf.d/shurl.conf
COPY ./tests/examples/nginx/docker-entrypoint.sh /docker-entrypoint.d/70-shurl-sync.sh
RUN chmod a+x /docker-entrypoint.d/*.sh
EXPOSE 80
EXPOSE 443

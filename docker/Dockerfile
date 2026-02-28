FROM python:3.13-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN groupadd --system user && \
    useradd --system --gid user --create-home user && \
    mkdir -m 755 -p /app && \
    chown user:user /app

WORKDIR /app

USER user

# Set environment variables to prevent Python from writing .pyc files, ensure that output is not buffered,
# and to disable UV's development mode
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_NO_DEV=1

COPY --chown=user:user --chmod=700 src /app/src
COPY --chown=user:user --chmod=700 pyproject.toml uv.lock /app/

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "estude.wsgi:application", "--bind", "0.0.0.0:8000", "--chdir", "src"]

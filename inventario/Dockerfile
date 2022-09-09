FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /code

# Install Poetry and copy poetry.lock* to /code in case it doesn't exist
RUN apt clean && apt update && apt install libsndfile1 ffmpeg  -y

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /code/
RUN poetry install --no-root --no-dev
ENV PYTHONPATH=/code
EXPOSE 8000
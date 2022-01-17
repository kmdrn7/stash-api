FROM python:3.9

WORKDIR /code

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

ENV JSON_LOGS=True \
    LOG_LEVEL="INFO" \
    BIND_HOST="0.0.0.0" \
    BIND_PORT="8000" \
    WORKERS=2

COPY main.py entrypoint.py /code/
COPY app /code/app

CMD ["python", "entrypoint.py"]

EXPOSE 8000

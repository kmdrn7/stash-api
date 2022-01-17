FROM python:3.9

WORKDIR /code

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY main.py /code/
COPY app /code/app

CMD [ "gunicorn", "main:app", \
    "-k", "uvicorn.workers.UvicornWorker", \
    "--bind", "0.0.0.0:8000" \
]

EXPOSE 8000

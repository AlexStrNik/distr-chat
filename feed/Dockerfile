FROM python:3.11

WORKDIR /feed

RUN python3 -m pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY app app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--root-path", "/feed"]


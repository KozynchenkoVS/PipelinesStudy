FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/pipelines
RUN mkdir /app/example_pipeline
RUN mkdir /app/tests

COPY /pipelines /app/pipelines
COPY /example_pipeline /app/example_pipeline
COPY /tests /app/tests
COPY pyproject.toml /app
COPY setup.py /app
COPY execute_pipelines.sh /app
COPY poetry.lock /app
COPY README.md /app


RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT [ "sh", "/app/execute_pipelines.sh" ]

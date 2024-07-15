FROM python:3.12
LABEL maintainer="muhammad najam"
RUN pip install poetry
WORKDIR /code
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY . /code/
RUN poetry config virtualenvs.create false
RUN poetry install 
EXPOSE 8000
ENTRYPOINT [ "poetry", "run", "uvicorn","imtiaz_mart_api.main:app","--host","0.0.0.0", "--reload"]
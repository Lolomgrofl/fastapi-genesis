FROM python:3.10.2-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc g++ curl procps net-tools tini

# Set up the Poetry environment
ENV POETRY_HOME=/tmp/poetry
RUN curl -sSL https://install.python-poetry.org/ | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH

# Set up the Python environment
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the project root
COPY pyproject.toml poetry.lock /app/

# Install the project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --only main --no-root --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app/

# Expose the application port
EXPOSE 8000

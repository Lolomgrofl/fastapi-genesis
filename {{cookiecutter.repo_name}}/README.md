## Pre-requisites

Before getting started, please ensure that you have the following dependencies installed on your system:

- Docker: [Installation guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation guide](https://docs.docker.com/compose/install/)
- Poetry: [Installation guide](https://python-poetry.org/docs/#installation)

## Getting Started

To set up and run the app, please follow these steps:

1. Move to the directory where `pyproject.toml` is located:

   ```shell
   cd {{ cookiecutter.repo_name }}
   ```
2. Install the dependencies:

   ```shell
   poetry install
   ```

   If you don't want to install the dev packages,
   you can use the following command instead:
   ```shell
   poetry install --without dev
   ```

3. Activate the virtual environment:

   ```shell
   poetry shell
   ```

4. All necessary commands to start with the project can be found in Makefile.
   To see all available commands, run the following command:

   ```shell
   make help
   ```

5. Build and start the Docker containers:

   ```shell
   make build
   ```

6. Open your browser and go to `http://localhost:{{ cookiecutter.app_service_port }}` to see the app running.

7. Since there is only one SQLAlchemy model, you can create a new migration file by running the following command:

   ```shell
   make autogenerate msg="user_init"
   ```

   This will create a new migration file in `{{ cookiecutter.repo_name }}/alembic/versions/`.

   Since the `app` service inside `docker-compose.yaml` will automatically run the `alembic upgrade head` command whenever it starts, in order to apply the new migration, you just need to stop the containers and start them again. CTRL+C to stop the containers and then run the following command to start them again:
   ```shell
   make up
   ```

8. To check the documentation of the API, go to `http://localhost:{{ cookiecutter.app_service_port }}/docs`.

9. To check the database you can use hosted `pgAdmin` tool, just go to `http://localhost:{{ cookiecutter.pgadmin_service_port }}` and login with the credentials from `.env` file:
   - Email: `$PGADMIN_EMAIL`
   - Password: `$PGADMIN_PASSWORD`

# ENJOY AND GOOD LUCK WITH YOUR PROJECT! 🧬 🚀

# FastAPI Genesis 🧬 - Project Template Generator 🚀
Simple FastAPI project template with Docker, Alembic, PostgreSQL, Poetry and pre-commit to kickstart your new projects.

## How to use it 🤓

Go to the directory where you want to create your project and run:

```bash
pip install cookiecutter
cookiecutter https://github.com/Lolomgrofl/fastapi-genesis.git
```

## What's included in the template 🎉

- Here is an explanation of the directory structure of the template:
```
├── alembic                 <- Alembic migrations
│
├── app                     <- Source code of the application (the main package)
│   ├── daos                <- Data Access Objects (DAOs) to interact with the database
│   ├── models              <- SQLAlchemy models (the database schema)
│   ├── routers             <- FastAPI routers (endpoints)
│   ├── schemas             <- Pydantic schemas for request and response models
│   ├── services            <- Business logic layer (services)
│   ├── db.py               <- Database initialization and session management code
│   ├── main.py             <- FastAPI application instance and startup code
│   └── settings.py         <- Settings management code (using pydantic settings)
│
├── scripts                 <- Scripts to perform various tasks like alembic migrations, etc.
│
├── static                  <- Static files like images, documents, etc.
│
├── tests                   <- Unit tests, one subdirectory per application module
│
├── .env                    <- Environment variables. Should not be committed to VCS
│
├── .gitignore              <- Files and directories to be ignored by git
│
├── .pre-commit-config.yaml <- Configuration of pre-commit hooks (see https://pre-commit.com/)
│
├── alembic.ini             <- Alembic configuration file
│
├── docker-compose.yml      <- Docker compose configuration file
│
├── Dockerfile              <- Dockerfile for building the image of the application
│
├── Makefile                <- Makefile with useful commands for development and project setup
│
├── pyproject.toml          <- Python dependencies for Poetry (see https://python-poetry.org/)
│
├── README.md               <- File with useful information about the project and how to use it
```

## Features 🧩

- **Docker** and **docker-compose** for local development
- **FastAPI** application with **uvicorn** server
- **AsyncPG** for asynchronous access to PostgreSQL
- **Pydantic** for data validation
- **Poetry** for managing Python dependencies
- **Alembic** for database migrations
- **Pre-commit** hooks for code formatting and linting
- **JWT** token authentication
- **SQLAlchemy** models
- **CORS** (Cross Origin Resource Sharing)

## User flow as an example of how to use the template 💡

- It consists of the following steps:
```
    - Register a new user
    - Login with the new user
    - Get all users
    - Delete all users
```
- This following example will show you the pattern and good practices to follow in order to continue developing your application.


## Cookiecutter parameters explained 🍪


- `repo_name`: Name of the project repository (e.g. `my_project`)
- `app_container_name`: Name of the Docker container for the FastAPI application server inside `docker-compose.yaml` file
- `app_service_port`: Port on the host machine to which the FastAPI application will be exposed inside `docker-compose.yaml` file and `Dockerfile`
- `db_container_name`: Name of the Docker container for the PostgreSQL database server inside `docker-compose.yaml` file
- `db_service_port`: Port on the host machine to which the PostgreSQL database server will be exposed inside `docker-compose.yaml` file
- `pgadmin_container_name`: Name of the Docker container for the pgAdmin web interface inside `docker-compose.yaml` file
- `pgadmin_service_port`: Port on the host machine to which the pgAdmin web interface will be exposed inside `docker-compose.yaml` file
- `network_name`: Name of the Docker network that will be created inside `docker-compose.yaml` file

# GLHF 🚀

## License

This project is licensed under the terms of the MIT license.

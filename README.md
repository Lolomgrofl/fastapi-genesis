# FastAPI Genesis - Project Template Generator 🚀
Simple FastAPI project template with Docker, Alembic, PostgreSQL, Poetry and pre-commit

## How to use it

Go to the directory where you want to create your project and run:

```bash
pip install cookiecutter
cookiecutter https://github.com/Lolomgrofl/fastapi_genesis.git
```

## What's included in the template

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
├── pyproject.toml          <- Python dependencies for Poetry (see https://python-poetry.org/)
│
├── README.md               <- File with useful information about the project and how to use it
│
└── setup.cfg               <- Configuration of various tools (pytest, flake8, black, isort)
```

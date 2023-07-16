#!/bin/bash
docker-compose exec app alembic revision --autogenerate -m $1

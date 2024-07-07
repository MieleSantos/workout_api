#!/bin/sh

# Executa as migrações do banco de dados
# alembic upgrade head

poetry run uvicorn --host 0.0.0.0 workout_api.main:app
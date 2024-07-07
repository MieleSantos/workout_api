# FastAPI
### Quem é o FastAPi?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.


## Execução da API

Para executar o projeto, utilizei o [poetry](https://python-poetry.org/).Com o poetry instalado, execute o comando para instalar as dependências:

```bash
poetry install
```

Crie um arquivo `.env` na raiz do projeto, para especifica a url para conecta com o banco de dados, exemplo
de  url:
```
DB_URL="postgresql+asyncpg://workout:workout@db:5432/workout"
```

A APi esta configurada para ser executada no container docker, para executa, use o comando:

```
docker compose up --build -d
```



Esse comando vai subir os container do banco de dados e da api, depois precisa fazer as migrações no banco, para isso
ative o `env` com `poetry shell` e execute:


```bash
task upgrade_alembic
```

> **Nota:** task são tarefas configuradas usando a biblioteca [taskipy](https://github.com/taskipy/taskipy) para automatiza tarefas, ela esta configurada no `pyproject.tmol` na seção `[tool.taskipy.tasks]`, onde tem os comando mapeados

Além das migrações no taskipy, tem comando para fazer as formatações e lint 

Com os container executando e as migrações feitas, basta acessa: `http://127.0.0.1:8000/docs` para acessa a documentação do swagger e testa a api


# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/
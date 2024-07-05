from pydantic import Field
from pydantic_settings import BaseSettings

# HOST = os.environ["HOST_IP"]


class Settings(BaseSettings):
    DB_URL: str = Field(
        default='postgresql+asyncpg://workout:workout@172.18.111.176/workout'
    )


settings = Settings()

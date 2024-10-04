from typing import Annotated

from pydantic import BeforeValidator, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors_origins(variable: str) -> list[str]:
    if isinstance(variable, str):
        return [item.strip() for item in variable.split(",")]

    raise ValueError(variable)


class Settings(BaseSettings):
    # main postgres db settings
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    ECHO_SQL: bool

    @computed_field
    @property
    def postgres_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )

    # testing postgres db settings
    TEST_DB_USER: str
    TEST_DB_PASSWORD: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str
    
    @computed_field
    @property
    def testing_postgres_url(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql",
            username=self.TEST_DB_USER,
            password=self.TEST_DB_PASSWORD,
            host=self.TEST_DB_HOST,
            port=self.TEST_DB_PORT,
            path=self.TEST_DB_NAME,
        )
    
    # CORS settings
    CORS_ORIGINS: Annotated[str | list, BeforeValidator(parse_cors_origins)] = []

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()

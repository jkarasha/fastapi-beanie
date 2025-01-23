from typing import Any
from pydantic import MongoDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class CustomBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

class Config(CustomBaseSettings):
    
    DATABASE_URL: str = ""
    DATABASE_NAME: str = ""
    COLLECTION_NAME: str = ""
    #
    CORS_ORIGINS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str] = ["*"]

    APP_VERSION: str = "0.1"

settings = Config()
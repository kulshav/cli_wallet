import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PATH_TO_STORAGE: str
    DEBUG_LOG_PATH: str


settings = Settings()

if __name__ == "__main__":
    print(settings.PATH_TO_STORAGE)

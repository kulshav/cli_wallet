import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TEST_MODE: bool = True  # Default = False on production

    env_file: str = ".test.env" if TEST_MODE else ".env"
    env_file_path: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", env_file)
    )

    model_config = SettingsConfigDict(env_file=env_file_path, extra="ignore")

    PATH_TO_STORAGE: str


settings = Settings()

if __name__ == '__main__':
    print(settings.PATH_TO_STORAGE)

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    #variables de redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: str
    REDIS_UI_PORT : int


settings = Settings()

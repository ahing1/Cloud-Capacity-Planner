from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App
    APP_ENV: str = "dev"
    LOG_LEVEL: str = "INFO"

    # DB (async for FastAPI runtime)
    DATABASE_URL: str

    # DB (sync for Alembic migrations)
    ALEMBIC_DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()

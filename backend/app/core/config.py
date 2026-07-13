from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AIEP"
    app_version: str = "0.1.0"

    host: str = "127.0.0.1"
    port: int = 8000

    log_level: str = "INFO"

    llm_provider: str = "gemini"

    database_url: str = "sqlite:///aiep.db"

    gemini_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = Field(validation_alias="API_NAME")
    APP_VERSION: str = Field(validation_alias="API_VERSION")
    OPENAI_API_KEY: str = Field(validation_alias="OpenAI_API_KEY")

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int = Field(validation_alias="FILE_CHUNK_SIZE")
    mongo_url: str
    mongodb_name: str

    # This is the correct Pydantic v2 way to load your .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # This prevents crashes from extra unmapped items
    )

def get_settings():
    return Settings()
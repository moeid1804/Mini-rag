from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    API_NAME: str
    API_VERSION: str
    OpenAI_API_KEY: str

    FILE_ALLOWED_TYPES: list  
    FILE_MAX_SIZE: int

    class Config:
        env_file = '.env'

def get_settings():
    return Settings()        
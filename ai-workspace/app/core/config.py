from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY:str="actual_production_secret_key_here"
    ALGORITHM:str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int=15
    REFRESH_TOKEN_EXPIRE_DAYS:int=30
    DATABASE_URL:str

    model_config=SettingsConfigDict(
        env_file=".env"
    )

settings=Settings()
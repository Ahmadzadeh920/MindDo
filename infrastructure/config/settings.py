import os 
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()

class Settings(BaseSettings):
    # Allow unknown env variables
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    # Application
    APP_NAME: str = Field("MindDo", env="APP_NAME")
    ENV: str = Field("development", env="ENV")
    email_sender: str = Field("noreply@minddo.com", env="EMAIL_SENDER")


    # Database
    DB_HOST: str = Field("db", env="DB_HOST")        # matches docker-compose service name
    DB_PORT: int = Field(5432, env="DB_PORT")
    DB_USER: str = Field("postgres", env="DB_USER")
    DB_PASSWORD: str = Field("postgres", env="DB_PASSWORD")
    DB_NAME: str = Field("minddo", env="DB_NAME")

    # SMTP
    SMTP_HOST: str = Field("smtp4dev", env="SMTP_HOST")
    SMTP_PORT: int = Field(25, env="SMTP_PORT")
    SMTP_FROM: str = Field("noreply@minddo.com", env="SMTP_FROM")

    # JWT / Auth
    SECRET_KEY: str = Field("super-secret-key", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    
    # Redis
    REDIS_HOST: str = Field("redis", env="REDIS_HOST")  # matches docker-compose service name
    REDIS_PORT: int = Field(6379, env="REDIS_PORT")
    @property
    def DATABASE_URL(self) -> str:
        # SQLAlchemy-compatible URL
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


settings = Settings()

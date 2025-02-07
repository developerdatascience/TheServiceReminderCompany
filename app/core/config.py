from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./servicereminder.db"
    SECRET_KEY: str = "your_secret_key"
    ALORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = "harendra263@gmail.com"
    SMTP_PASSWORD: str = "some_password"

    class Config:
        env_file = ".env"

settings = Settings()
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    UPLOAD_FOLDER: str = "uploads"

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure upload folder exists
os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)



# class Settings(BaseSettings):
#     DATABASE_URL: str = "sqlite:///./test.db"
#     SECRET_KEY: str = "supersecret"
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

#     class Config:
#         env_file = ".env"


# settings = Settings()

# # from pydantic import BaseSettings as old version
# from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     SECRET_KEY = "supersecret"
#     ALGORITHM = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES = 60

#     DB_URL = "mysql+pymysql://root:password@localhost/fastapi_db"

# settings = Settings()

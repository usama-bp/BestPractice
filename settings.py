from typing import ClassVar
from pydantic_settings import BaseSettings
# from pydantic import Cla
from dotenv import load_dotenv
import os


# username:str=os.getenv("USERNAME")
# password:str=os.getenv("PASSWORD")
# # port:str=os.getenv("PORT")
# host:str=os.getenv("HOST")
# db_name:str=os.getenv("DATABASE_NAME")
load_dotenv()

DB_URL=os.getenv("DB_URL")


class Settings(BaseSettings):
    # Database settings
    # database_url: str = "sqlite:///.db"
    database_url:ClassVar[str]= DB_URL


    # API settings
    api_version: ClassVar[str]=os.getenv("VERSION")
    debug: ClassVar[bool] = os.getenv("DEBUG")

    # Security settings
    secret_key: ClassVar[str] = os.getenv("SECRET_KEY")
    algorithm: ClassVar[str] = os.getenv("ALGORITHM")
    access_token_expire_minutes: ClassVar[int] = os.getenv("ACCESS_EXPIRE_TOKEN_TIME")

    # Logging settings
    log_level: ClassVar[str] = os.getenv("LOG_LEVEL")
    class config:
        ignored_types=['database_url']


# Create an instance of the Settings class

if __name__=="__main__":
    
    settings = Settings()

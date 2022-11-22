"""Configuration for the project, contains project name, project slug. The
project slug is used as the centralized logger name."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Youtube Downloader'
    PROJECT_SLUG: str = 'ytb_downloader'


settings = Settings()

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Youtube Downloader'
    PROJECT_SLUG: str = 'ytb_downloader'


settings = Settings()

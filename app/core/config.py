from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Stash API"
    LOGGER_NAME: str = APP_NAME.replace(" ", "-").lower()


settings = Settings()

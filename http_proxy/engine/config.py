import pathlib

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TARGET_URL: AnyHttpUrl
    LOG_LEVEL: str = "DEBUG"
    HTTP_PORT: int = 8080
    SECRET_KEY: str
    TIMEOUT: float = 10.0
    MAX_BODY: float = 5

    class Config:
        env_file = pathlib.Path(pathlib.Path(__file__).parent.parent.parent, ".env")

    @property
    def target_url(self):
        return str(settings.TARGET_URL)

    @property
    def max_body_in_bytes(self):
        return self.MAX_BODY * (10**6)


settings = Settings()

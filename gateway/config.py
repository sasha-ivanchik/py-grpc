from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

env_filename = "example.env"
load_dotenv(find_dotenv(env_filename))

BASE_DIR = Path.cwd().resolve().parent
env_path = BASE_DIR / env_filename


class GrpcSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path, env_file_encoding="utf-8", extra="allow"
    )

    ITEM_GRPC_ADDRESS: str
    ITEM_GRPC_IN_DOCKER_URL: str
    AUTH_GRPC_IN_DOCKER_URL: str
    AUTH_GRPC_ADDRESS: str


settings = GrpcSettings()

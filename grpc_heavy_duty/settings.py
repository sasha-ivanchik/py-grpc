from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path.cwd().resolve().parent
env_path = BASE_DIR / "example.env"


class GrpcSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path, env_file_encoding="utf-8", extra="allow"
    )

    HEAVY_DUTY_GRPC_ADDRESS: str
    HEAVY_DUTY_GRPC_IN_DOCKER_URL: str


settings = GrpcSettings()

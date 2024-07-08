from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path.cwd().resolve().parent
env_path = BASE_DIR / "example.env"


class GrpcSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path, env_file_encoding="utf-8", extra="allow"
    )

    AUTH_GRPC_ADDRESS: str
    ACCESS_TOKEN_EXPIRE_SEC: int
    TOKEN_ENCRYPTION_SECRET: str
    TOKEN_ENCRYPTION_SALT: str
    ALGORITHM: str

    HEAVY_DUTY_GRPC_ADDRESS: str
    HEAVY_DUTY_GRPC_IN_DOCKER_URL: str


settings = GrpcSettings()

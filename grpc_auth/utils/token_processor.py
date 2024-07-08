from typing import Union
from datetime import datetime, timedelta

import jwt

from settings import settings


class TokenProcessor:
    @staticmethod
    def create_jwt(
            token_payload: dict,
            expire_timedelta_sec: int | None = settings.ACCESS_TOKEN_EXPIRE_SEC,
            expire_timedelta_days: int | None = None,
    ) -> str:
        return TokenProcessor.encode_jwt(
            payload=token_payload,
            expire_timedelta_sec=expire_timedelta_sec,
            expire_timedelta_days=expire_timedelta_days,
        )

    @staticmethod
    def encode_jwt(
            payload: dict,
            private_key: str = settings.TOKEN_ENCRYPTION_SECRET,
            algorithm: str = settings.ALGORITHM,
            expire_timedelta_sec: int | None = settings.ACCESS_TOKEN_EXPIRE_SEC,
            expire_timedelta_days: int | None = None,
    ) -> str:
        to_encode = payload.copy()
        expire = (
            datetime.utcnow() + timedelta(seconds=expire_timedelta_sec)
            if expire_timedelta_sec
            else datetime.utcnow() + timedelta(days=expire_timedelta_days)
        )
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(
            to_encode,
            private_key,
            algorithm,
        )
        return encoded_jwt

    @staticmethod
    def decode_jwt(
            encoded_token: Union[str, bytes],
            public_key: str = settings.TOKEN_ENCRYPTION_SECRET,
            algorithm: str = settings.ALGORITHM,
    ):

        encoded_jwt = jwt.decode(
            encoded_token,
            public_key,
            algorithms=[algorithm],
        )
        return encoded_jwt

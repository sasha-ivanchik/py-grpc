from enum import Enum

from pydantic import BaseModel


class BaseItem(BaseModel):
    name: str
    is_simple: bool
    sample_int: int


class CreateItem(BaseItem):
    pass


class ReadItem(BaseItem):
    id: int


class ResponseStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class Token(BaseModel):
    token: str


class User(BaseModel):
    id: int
    username: str


class UserCompliment(BaseModel):
    user: User
    message: str


class BackendResponse(BaseModel):
    items: list[ReadItem | None]
    user: UserCompliment


class GatewayResponse(BaseModel):
    status: ResponseStatus
    data: ReadItem | None | str | Token | UserCompliment | BackendResponse

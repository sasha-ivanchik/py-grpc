from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("id", "name", "is_simple", "sample_int", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_INT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    is_simple: bool
    sample_int: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., is_simple: bool = ..., sample_int: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class CreateItemRequest(_message.Message):
    __slots__ = ("name", "is_simple", "sample_int", "user_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_INT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_simple: bool
    sample_int: int
    user_id: int
    def __init__(self, name: _Optional[str] = ..., is_simple: bool = ..., sample_int: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class CreateItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class ListItemsRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class ListItemsResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class GetItemRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ("id", "name", "is_simple", "sample_int", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_INT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    is_simple: bool
    sample_int: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., is_simple: bool = ..., sample_int: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class UpdateItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class DeleteItemRequest(_message.Message):
    __slots__ = ("id", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class DeleteItemResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: str
    def __init__(self, success: _Optional[str] = ...) -> None: ...

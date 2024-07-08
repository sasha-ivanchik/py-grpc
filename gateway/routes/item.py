from fastapi import APIRouter, status, Depends, HTTPException, Header
from fastapi.responses import ORJSONResponse
from google.protobuf.json_format import MessageToDict
from grpc.aio._call import AioRpcError

from schemas import (
    CreateItem,
    ReadItem,
    GatewayResponse,
    BackendResponse,
    UserCompliment,
    ResponseStatus,
)
from protos import (
    item_pb2_grpc,
    auth_pb2_grpc,
)
from protos import (
    item_pb2,
)
from grpcs_clients.item_grpc import grpc_item_client
from grpcs_clients.auth_grpc import grpc_auth_client
from services.auth import AuthService

router = APIRouter(prefix="/item", tags=["item"])


@router.post(
    "/items",
    status_code=status.HTTP_201_CREATED,
    response_model=GatewayResponse,
    response_class=ORJSONResponse
)
async def create_item(
        item: CreateItem,
        auth: str = Header(None),
        item_client: item_pb2_grpc.ItemServiceStub = Depends(grpc_item_client),
        auth_client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    user = await AuthService.get_user_by_token(
        token=auth,
        auth_client=auth_client
    )

    try:
        grpc_response = await item_client.Create(
            item_pb2.CreateItemRequest(
                name=item.name,
                is_simple=item.is_simple,
                sample_int=item.sample_int,
                user_id=user.data.user.id,
            ), timeout=5
        )

    except AioRpcError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.debug_error_string()
        )

    response_dict = MessageToDict(grpc_response)
    new_item = response_dict.get("item")
    items = [ReadItem(
        id=int(new_item.get("id")),
        name=new_item.get("name"),
        is_simple=True if new_item.get("isSimple") else False,
        sample_int=int(new_item.get("sampleInt")),
    ), ]

    return GatewayResponse(
        status=ResponseStatus.SUCCESS,
        data=BackendResponse(
            items=items,
            user=user.data,
        )
    )


@router.get(
    "/items",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def list_items(
        auth: str = Header(None),
        item_client: item_pb2_grpc.ItemServiceStub = Depends(grpc_item_client),
        auth_client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    user = await AuthService.get_user_by_token(
        token=auth,
        auth_client=auth_client
    )

    try:
        grpc_response = await item_client.List(
            item_pb2.ListItemsRequest(
                user_id=user.data.user.id,
            ),
            timeout=5,
        )
    except AioRpcError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.details()
        )

    response_dict = MessageToDict(grpc_response)
    list_of_items = response_dict.get("items")

    items = [
        ReadItem(
            id=int(item.get("id")),
            name=item.get("name"),
            is_simple=True if item.get("isSimple") else False,
            sample_int=int(item.get("sampleInt")),
        )
        for item in list_of_items
    ]

    return GatewayResponse(
        status=ResponseStatus.SUCCESS,
        data=BackendResponse(
            items=items,
            user=user.data,
        )
    )


@router.get(
    "/items/{item_id}",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def get_item(
        item_id: int,
        auth: str = Header(None),
        item_client: item_pb2_grpc.ItemServiceStub = Depends(grpc_item_client),
        auth_client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    user = await AuthService.get_user_by_token(
        token=auth,
        auth_client=auth_client
    )

    try:
        grpc_response = await item_client.Get(
            item_pb2.GetItemRequest(id=item_id, user_id=user.data.user.id),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.details()
        )
    response_dict = MessageToDict(grpc_response)
    item = response_dict.get("item")

    items = [ReadItem(
        id=int(item.get("id")),
        name=item.get("name"),
        is_simple=True if item.get("isSimple") else False,
        sample_int=int(item.get("sampleInt")),
    ), ]

    return GatewayResponse(
        status=ResponseStatus.SUCCESS,
        data=BackendResponse(
            items=items,
            user=user.data,
        )
    )


@router.delete(
    "/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_item(
        item_id: int,
        auth: str = Header(None),
        item_client: item_pb2_grpc.ItemServiceStub = Depends(grpc_item_client),
        auth_client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
):
    user = await AuthService.get_user_by_token(
        token=auth,
        auth_client=auth_client
    )
    try:
        await item_client.Delete(
            item_pb2.DeleteItemRequest(id=item_id, user_id=user.data.user.id),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.details()
        )


@router.put(
    "/items/{item_id}",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def update_item(
        item_id: int,
        item: CreateItem,
        auth: str = Header(None),
        item_client: item_pb2_grpc.ItemServiceStub = Depends(grpc_item_client),
        auth_client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    user = await AuthService.get_user_by_token(
        token=auth,
        auth_client=auth_client
    )

    try:
        grpc_response = await item_client.Update(
            item_pb2.UpdateItemRequest(
                id=item_id,
                name=item.name,
                is_simple=item.is_simple,
                sample_int=item.sample_int,
                user_id=user.data.user.id,
            ),
            timeout=5
        )
    except AioRpcError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.details()
        )

    response_dict = MessageToDict(grpc_response)
    new_item = response_dict.get("item")

    items = [ReadItem(
        id=int(new_item.get("id")),
        name=new_item.get("name"),
        is_simple=True if new_item.get("isSimple") else False,
        sample_int=int(new_item.get("sampleInt")),
    ), ]

    return GatewayResponse(
        status=ResponseStatus.SUCCESS,
        data=BackendResponse(
            items=items,
            user=user.data,
        )
    )

from __future__ import annotations

from fastapi import (
    APIRouter,
    Form,
    Depends,
    Header,
)
from fastapi.responses import ORJSONResponse

from grpcs_clients.auth_grpc import grpc_auth_client
from protos import auth_pb2_grpc
from schemas import GatewayResponse
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def log_in_for_access_token(
        username: str = Form(),
        password: str = Form(),
        client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    return await AuthService.log_in(
        username=username,
        password=password,
        client=client
    )


@router.post(
    "/signup",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def sign_up_for_access_token(
        username: str = Form(),
        password: str = Form(),
        client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    return await AuthService.sign_up(
        username=username,
        password=password,
        client=client
    )


@router.get(
    "/me",
    response_model=GatewayResponse,
    response_class=ORJSONResponse,
)
async def get_self_info(
        auth: str = Header(None),
        client: auth_pb2_grpc.AuthServiceStub = Depends(grpc_auth_client),
) -> GatewayResponse:
    return await AuthService.get_user_by_token(
        token=auth,
        auth_client=client
    )

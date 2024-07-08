from fastapi import Depends, HTTPException
from google.protobuf.json_format import MessageToDict
from grpc.aio import AioRpcError
from starlette import status

from protos import auth_pb2_grpc, auth_pb2
from schemas import GatewayResponse, ResponseStatus, UserCompliment, User, Token


class AuthService:
    @staticmethod
    async def _get_user_by_token(
            auth_token: str,
            client: auth_pb2_grpc.AuthServiceStub,
    ) -> GatewayResponse:
        try:

            grpc_response = await client.ValidateToken(
                auth_pb2.ValidateTokenRequest(
                    token=auth_token
                ), timeout=5
            )

        except AioRpcError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=e.details()
            )

        response_dict = MessageToDict(grpc_response)

        user_data = response_dict.get("user")
        return GatewayResponse(
            status=ResponseStatus.SUCCESS,
            data=UserCompliment(
                user=User(
                    id=user_data.get("id"),
                    username=user_data.get("username")
                ),
                message=response_dict.get("message").get("message"),
            ),
        )

    @staticmethod
    async def sign_up(
            username: str,
            password: str,
            client: auth_pb2_grpc.AuthServiceStub,
    ) -> GatewayResponse:
        try:
            grpc_response = await client.Signup(
                auth_pb2.LoginRequest(
                    username=username,
                    password=password,
                ), timeout=5
            )

        except AioRpcError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=e.details()
            )

        response_dict = MessageToDict(grpc_response)
        new_item = response_dict.get("token")

        return GatewayResponse(
            status=ResponseStatus.SUCCESS,
            data=Token(token=new_item.get("token")),
        )

    @staticmethod
    async def log_in(
            username: str,
            password: str,
            client: auth_pb2_grpc.AuthServiceStub,
    ) -> GatewayResponse:
        try:
            grpc_response = await client.Login(
                auth_pb2.LoginRequest(
                    username=username,
                    password=password,
                ), timeout=5
            )
        except AioRpcError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=e.details()
            )

        response_dict = MessageToDict(grpc_response)
        new_item = response_dict.get("token")

        return GatewayResponse(
            status=ResponseStatus.SUCCESS,
            data=Token(token=new_item.get("token")),
        )

    @staticmethod
    async def get_user_by_token(
            token: str,
            auth_client: auth_pb2_grpc.AuthServiceStub,
    ) -> GatewayResponse:
        unauthorized_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )

        if not token:
            raise unauthorized_exception

        user = await AuthService._get_user_by_token(
            auth_token=token,
            client=auth_client
        )

        if user.status != ResponseStatus.SUCCESS:
            raise unauthorized_exception

        return user

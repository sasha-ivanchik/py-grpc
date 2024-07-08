from grpc import aio, StatusCode

from protos import auth_pb2
from protos import auth_pb2_grpc
from protos import heavy_duty_pb2
from db.models import User
from utils.hash_helper import Hasher
from utils.token_processor import TokenProcessor
from grpc_clients.heavy_duty_grpc import grpc_heavy_duty_client


class AuthService(auth_pb2_grpc.AuthServiceServicer):
    async def Login(
            self,
            request: auth_pb2.LoginRequest,
            context: aio.ServicerContext,
    ):
        try:
            incoming_user = await User.select().where(
                User.username == request.username,
            ).first()
        except Exception:
            await context.abort(
                code=StatusCode.PERMISSION_DENIED,
                details='Bad request. Check your request and try again.'
            )
        if (incoming_user is None) or (not Hasher.verify_password(
                plain_password=request.password,
                hashed_password=incoming_user.get('hashed_password')
        )):
            await context.abort(
                code=StatusCode.PERMISSION_DENIED,
                details='Bad request. Check your request and try again.'
            )

        payload = {
            'username': incoming_user.get('username'),
            'id': incoming_user.get('id'),
        }

        token = auth_pb2.Token(
            token=TokenProcessor.create_jwt(token_payload=payload)
        )

        return auth_pb2.LoginResponse(token=token)

    async def Signup(
            self,
            request: auth_pb2.LoginRequest,
            context: aio.ServicerContext
    ):
        try:
            new_user = User(
                username=request.username,
                hashed_password=Hasher.get_password_hash(request.password)
            )
            await new_user.save()
        except Exception as e:
            await context.abort(
                code=StatusCode.PERMISSION_DENIED,
                details=f'Bad request. Check your request and try again.'
            )
        if new_user is None:
            await context.abort(
                code=StatusCode.PERMISSION_DENIED,
                details=f'Bad request. Check your request and try again.'
            )

        return await self.Login(request, context)

    async def ValidateToken(
            self,
            request: auth_pb2.ValidateTokenRequest,
            context: aio.ServicerContext
    ):

        incoming_token = request.token
        decoded_token_data = TokenProcessor.decode_jwt(encoded_token=incoming_token)
        user_id = decoded_token_data.get('id')
        user_username = decoded_token_data.get('username')

        heavy_duty_client = await grpc_heavy_duty_client()

        message = await heavy_duty_client.HeavyDuty(
            heavy_duty_pb2.HeavyDutyRequest(
                user=heavy_duty_pb2.User(
                    id=user_id,
                    username=user_username,
                )
            )
        )

        return auth_pb2.ValidateTokenResponse(
            user=auth_pb2.User(
                id=user_id,
                username=user_username,
            ),
            message=auth_pb2.Message(message=message.message),  # type: ignore  # noqa: E501 message
        )

import grpc

from protos import auth_pb2_grpc
from config import settings


async def grpc_auth_client() -> auth_pb2_grpc.AuthServiceStub:
    channel = grpc.aio.insecure_channel(settings.AUTH_GRPC_IN_DOCKER_URL)
    client = auth_pb2_grpc.AuthServiceStub(channel)
    return client

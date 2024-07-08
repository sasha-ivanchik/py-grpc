import grpc

from protos import item_pb2_grpc
from config import settings


async def grpc_item_client() -> item_pb2_grpc.ItemServiceStub:
    channel = grpc.aio.insecure_channel(settings.ITEM_GRPC_IN_DOCKER_URL)
    client = item_pb2_grpc.ItemServiceStub(channel)
    return client

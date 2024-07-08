import grpc

from protos import heavy_duty_pb2_grpc
from settings import settings


async def grpc_heavy_duty_client() -> heavy_duty_pb2_grpc.HeavyDutyServiceStub:
    channel = grpc.aio.insecure_channel(settings.HEAVY_DUTY_GRPC_IN_DOCKER_URL)
    client = heavy_duty_pb2_grpc.HeavyDutyServiceStub(channel)
    return client

import asyncio

from grpc import aio

from server_grpc import HeavyDutyService
from protos import heavy_duty_pb2_grpc
from settings import settings


async def start_server(address: str) -> None:
    server = aio.server()
    heavy_duty_pb2_grpc.add_HeavyDutyServiceServicer_to_server(
        HeavyDutyService(), server
    )
    server.add_insecure_port(address)
    print(f"Run HeavyDuty server on: {address}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(start_server(settings.HEAVY_DUTY_GRPC_ADDRESS))

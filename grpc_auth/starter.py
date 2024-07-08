import asyncio

from grpc import aio

from server_grpc import AuthService
from protos import auth_pb2_grpc
from settings import settings
from db.models import User


async def start_server(address: str) -> None:
    # create table if not exists. TODO move it
    await User.create_table(if_not_exists=True)
    server = aio.server()
    auth_pb2_grpc.add_AuthServiceServicer_to_server(
        AuthService(), server
    )
    server.add_insecure_port(address)
    print(f"Run User server on: {address}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(start_server(settings.AUTH_GRPC_ADDRESS))

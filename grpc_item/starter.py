import asyncio

from grpc import aio

from server_grpc import ItemService
from protos import item_pb2_grpc
from config import settings
from db.models import Item


async def start_server(address: str) -> None:
    await Item.create_table(if_not_exists=True)
    server = aio.server()
    item_pb2_grpc.add_ItemServiceServicer_to_server(
        ItemService(), server
    )
    server.add_insecure_port(address)
    print(f"Run Item server on: {address}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(start_server(settings.ITEM_GRPC_ADDRESS))

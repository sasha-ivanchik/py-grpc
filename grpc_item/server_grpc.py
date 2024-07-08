from grpc import aio, StatusCode

from protos import item_pb2
from protos import item_pb2_grpc
from db.models import Item


class ItemService(item_pb2_grpc.ItemServiceServicer):
    async def Create(
            self,
            request: item_pb2.CreateItemRequest,
            context: aio.ServicerContext
    ):
        if request.sample_int in (0, '0'):
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='`sample_int` must be non-zero.'
            )
        try:
            item = Item(
                name=request.name,
                is_simple=request.is_simple,
                sample_int=request.sample_int,
                user_id=request.user_id,
            )
            await item.save()
        except Exception:
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='Bad request. Check your request and try again.'
            )
        return item_pb2.CreateItemResponse(item=item.to_dict())

    async def List(
            self,
            request: item_pb2.CreateItemRequest,
            context: aio.ServicerContext
    ):
        try:
            items = await Item.select().where(
                (Item.user_id == request.user_id) & (Item.user_id == request.user_id)
            )
            assert items is not None
        except Exception:
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='Bad request. Check your request and try again.'
            )
        return item_pb2.ListItemsResponse(items=items)

    async def Get(
            self,
            request: item_pb2.CreateItemRequest,
            context: aio.ServicerContext
    ):
        try:
            item = await Item.select().where(
                (Item.id == request.id) & (Item.user_id == request.user_id)
            ).first()
            assert item is not None
        except Exception:
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='Bad request. Check your request and try again.'
            )
        return item_pb2.GetItemResponse(item=item)

    async def Update(
            self,
            request: item_pb2.CreateItemRequest,
            context: aio.ServicerContext
    ):
        if request.sample_int in (0, '0'):
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='`sample_int` must be non-zero.'
            )
        try:
            await Item.update(
                {
                    Item.name: request.name,
                    Item.is_simple: request.is_simple,
                    Item.sample_int: request.sample_int
                }
            ).where(
                (Item.id == request.id) & (Item.user_id == request.user_id)
            )

            item = await Item.select().where(
                (Item.id == request.id) & (Item.user_id == request.user_id)
            ).first()
            assert item is not None
        except Exception:
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='Bad request. Check your request and try again.'
            )
        return item_pb2.UpdateItemResponse(item=item)

    async def Delete(
            self,
            request: item_pb2.CreateItemRequest,
            context: aio.ServicerContext
    ):
        try:
            await Item.delete().where(
                (Item.id == request.id) & (Item.user_id == request.user_id)
            )
        except Exception:
            await context.abort(
                code=StatusCode.INVALID_ARGUMENT,
                details='Bad request. Check your request and try again.'
            )
        return item_pb2.DeleteItemResponse(success='True')

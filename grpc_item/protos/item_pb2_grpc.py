# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from protos import item_pb2 as protos_dot_item__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protos/item_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ItemServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/item.ItemService/Create',
                request_serializer=protos_dot_item__pb2.CreateItemRequest.SerializeToString,
                response_deserializer=protos_dot_item__pb2.CreateItemResponse.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/item.ItemService/List',
                request_serializer=protos_dot_item__pb2.ListItemsRequest.SerializeToString,
                response_deserializer=protos_dot_item__pb2.ListItemsResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/item.ItemService/Get',
                request_serializer=protos_dot_item__pb2.GetItemRequest.SerializeToString,
                response_deserializer=protos_dot_item__pb2.GetItemResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/item.ItemService/Update',
                request_serializer=protos_dot_item__pb2.UpdateItemRequest.SerializeToString,
                response_deserializer=protos_dot_item__pb2.UpdateItemResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/item.ItemService/Delete',
                request_serializer=protos_dot_item__pb2.DeleteItemRequest.SerializeToString,
                response_deserializer=protos_dot_item__pb2.DeleteItemResponse.FromString,
                _registered_method=True)


class ItemServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ItemServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protos_dot_item__pb2.CreateItemRequest.FromString,
                    response_serializer=protos_dot_item__pb2.CreateItemResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protos_dot_item__pb2.ListItemsRequest.FromString,
                    response_serializer=protos_dot_item__pb2.ListItemsResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=protos_dot_item__pb2.GetItemRequest.FromString,
                    response_serializer=protos_dot_item__pb2.GetItemResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protos_dot_item__pb2.UpdateItemRequest.FromString,
                    response_serializer=protos_dot_item__pb2.UpdateItemResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=protos_dot_item__pb2.DeleteItemRequest.FromString,
                    response_serializer=protos_dot_item__pb2.DeleteItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'item.ItemService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('item.ItemService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ItemService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/item.ItemService/Create',
            protos_dot_item__pb2.CreateItemRequest.SerializeToString,
            protos_dot_item__pb2.CreateItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/item.ItemService/List',
            protos_dot_item__pb2.ListItemsRequest.SerializeToString,
            protos_dot_item__pb2.ListItemsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/item.ItemService/Get',
            protos_dot_item__pb2.GetItemRequest.SerializeToString,
            protos_dot_item__pb2.GetItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/item.ItemService/Update',
            protos_dot_item__pb2.UpdateItemRequest.SerializeToString,
            protos_dot_item__pb2.UpdateItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/item.ItemService/Delete',
            protos_dot_item__pb2.DeleteItemRequest.SerializeToString,
            protos_dot_item__pb2.DeleteItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

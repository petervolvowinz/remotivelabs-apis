# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import common_pb2 as common__pb2
from . import network_api_pb2 as network__api__pb2


class NetworkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeToSignals = channel.unary_stream(
                '/base.NetworkService/SubscribeToSignals',
                request_serializer=network__api__pb2.SubscriberConfig.SerializeToString,
                response_deserializer=network__api__pb2.Signals.FromString,
                )
        self.PublishSignals = channel.unary_unary(
                '/base.NetworkService/PublishSignals',
                request_serializer=network__api__pb2.PublisherConfig.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                )
        self.ReadSignals = channel.unary_unary(
                '/base.NetworkService/ReadSignals',
                request_serializer=network__api__pb2.SignalIds.SerializeToString,
                response_deserializer=network__api__pb2.Signals.FromString,
                )


class NetworkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SubscribeToSignals(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PublishSignals(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSignals(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeToSignals': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToSignals,
                    request_deserializer=network__api__pb2.SubscriberConfig.FromString,
                    response_serializer=network__api__pb2.Signals.SerializeToString,
            ),
            'PublishSignals': grpc.unary_unary_rpc_method_handler(
                    servicer.PublishSignals,
                    request_deserializer=network__api__pb2.PublisherConfig.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
            'ReadSignals': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSignals,
                    request_deserializer=network__api__pb2.SignalIds.FromString,
                    response_serializer=network__api__pb2.Signals.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'base.NetworkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SubscribeToSignals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/base.NetworkService/SubscribeToSignals',
            network__api__pb2.SubscriberConfig.SerializeToString,
            network__api__pb2.Signals.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PublishSignals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/base.NetworkService/PublishSignals',
            network__api__pb2.PublisherConfig.SerializeToString,
            common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSignals(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/base.NetworkService/ReadSignals',
            network__api__pb2.SignalIds.SerializeToString,
            network__api__pb2.Signals.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

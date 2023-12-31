# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nla_toolkit_pb2 as nla__toolkit__pb2


class LinearAlgebraServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PerformMatrixAddition = channel.unary_unary(
            "/nla_toolkit.LinearAlgebraService/PerformMatrixAddition",
            request_serializer=nla__toolkit__pb2.MatrixAdditionRequest.SerializeToString,
            response_deserializer=nla__toolkit__pb2.MatrixAdditionResponse.FromString,
        )
        self.PerformMatrixInversion = channel.unary_unary(
            "/nla_toolkit.LinearAlgebraService/PerformMatrixInversion",
            request_serializer=nla__toolkit__pb2.MatrixInverseRequest.SerializeToString,
            response_deserializer=nla__toolkit__pb2.MatrixInverseResponse.FromString,
        )


class LinearAlgebraServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PerformMatrixAddition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PerformMatrixInversion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_LinearAlgebraServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PerformMatrixAddition": grpc.unary_unary_rpc_method_handler(
            servicer.PerformMatrixAddition,
            request_deserializer=nla__toolkit__pb2.MatrixAdditionRequest.FromString,
            response_serializer=nla__toolkit__pb2.MatrixAdditionResponse.SerializeToString,
        ),
        "PerformMatrixInversion": grpc.unary_unary_rpc_method_handler(
            servicer.PerformMatrixInversion,
            request_deserializer=nla__toolkit__pb2.MatrixInverseRequest.FromString,
            response_serializer=nla__toolkit__pb2.MatrixInverseResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "nla_toolkit.LinearAlgebraService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class LinearAlgebraService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PerformMatrixAddition(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nla_toolkit.LinearAlgebraService/PerformMatrixAddition",
            nla__toolkit__pb2.MatrixAdditionRequest.SerializeToString,
            nla__toolkit__pb2.MatrixAdditionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def PerformMatrixInversion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/nla_toolkit.LinearAlgebraService/PerformMatrixInversion",
            nla__toolkit__pb2.MatrixInverseRequest.SerializeToString,
            nla__toolkit__pb2.MatrixInverseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

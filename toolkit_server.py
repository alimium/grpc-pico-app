"""server side stuff"""
from concurrent import futures
import numpy as np

import grpc
from grpc_types import nla_toolkit_pb2
from grpc_types import nla_toolkit_pb2_grpc
from utils import matrix_to_numpy, numpy_to_matrix


class LinearAlgebraServiceServer(nla_toolkit_pb2_grpc.LinearAlgebraServiceServicer):
    def PerformMatrixAddition(self, request, context):
        print("addition has been invoked!")
        array_a = matrix_to_numpy(request.matrix_a)
        array_b = matrix_to_numpy(request.matrix_b)
        response = nla_toolkit_pb2.MatrixAdditionResponse(
            result=numpy_to_matrix(array_a + array_b)
        )
        return response

    def PerformMatrixInversion(self, request, context):
        print("inversion has been invoked!")
        array = matrix_to_numpy(request.matrix)
        inverse = np.linalg.inv(array)
        response = nla_toolkit_pb2.MatrixInverseResponse(
            result=numpy_to_matrix(inverse)
        )
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nla_toolkit_pb2_grpc.add_LinearAlgebraServiceServicer_to_server(
        LinearAlgebraServiceServer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

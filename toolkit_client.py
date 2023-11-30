"""client side stuff"""
from grpc_types import nla_toolkit_pb2_grpc
from grpc_types import nla_toolkit_pb2
import time
import grpc
import numpy as np


def get_matrix(i: int) -> nla_toolkit_pb2.Matrix:
    print(f"Matrix {i}:")
    row = int(input("\thow many rows? "))
    col = int(input("\thow many cols? "))
    vals = [float(i) for i in input("\tenter elements: ").split(" ")]
    matrix = nla_toolkit_pb2.Matrix(values=vals, rows=row, cols=col)
    return matrix


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = nla_toolkit_pb2_grpc.LinearAlgebraServiceStub(channel)
        operation = int(
            input(
                "what operation do you want to do?\n\t1.addition\n\t2.inversion\nselect option: "
            )
        )
        if operation == 1:  # addition
            matrix_a = get_matrix(1)
            matrix_b = get_matrix(2)
            rqst = nla_toolkit_pb2.MatrixAdditionRequest(
                matrix_a=matrix_a, matrix_b=matrix_b
            )
            reply = stub.PerformMatrixAddition(rqst)
        elif operation == 2:  # inversion
            matrix = get_matrix(1)
            rqst = nla_toolkit_pb2.MatrixInverseRequest(matrix=matrix)
            reply = stub.PerformMatrixInversion(rqst)
        print(matrix_to_numpy(reply.result))


if __name__ == "__main__":
    run()

"""functions to make life easier!"""
import numpy as np
from grpc_types import nla_toolkit_pb2


def matrix_to_numpy(matrix: nla_toolkit_pb2.Matrix) -> np.ndarray:
    row = matrix.rows
    col = matrix.cols
    vals = list(matrix.values)
    return np.array(vals).reshape((row, col))


def numpy_to_matrix(array: np.ndarray) -> nla_toolkit_pb2.Matrix:
    row, col = array.shape
    matrix = nla_toolkit_pb2.Matrix(values=array.flatten(), rows=row, cols=col)
    return matrix

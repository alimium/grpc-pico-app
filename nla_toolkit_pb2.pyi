from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Matrix(_message.Message):
    __slots__ = ["values", "rows", "cols"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    rows: int
    cols: int
    def __init__(self, values: _Optional[_Iterable[float]] = ..., rows: _Optional[int] = ..., cols: _Optional[int] = ...) -> None: ...

class MatrixAdditionRequest(_message.Message):
    __slots__ = ["matrix_a", "matrix_b"]
    MATRIX_A_FIELD_NUMBER: _ClassVar[int]
    MATRIX_B_FIELD_NUMBER: _ClassVar[int]
    matrix_a: Matrix
    matrix_b: Matrix
    def __init__(self, matrix_a: _Optional[_Union[Matrix, _Mapping]] = ..., matrix_b: _Optional[_Union[Matrix, _Mapping]] = ...) -> None: ...

class MatrixAdditionResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: Matrix
    def __init__(self, result: _Optional[_Union[Matrix, _Mapping]] = ...) -> None: ...

class MatrixInverseRequest(_message.Message):
    __slots__ = ["matrix"]
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    matrix: Matrix
    def __init__(self, matrix: _Optional[_Union[Matrix, _Mapping]] = ...) -> None: ...

class MatrixInverseResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: Matrix
    def __init__(self, result: _Optional[_Union[Matrix, _Mapping]] = ...) -> None: ...

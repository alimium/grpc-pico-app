# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nla_toolkit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11nla_toolkit.proto\x12\x0bnla_toolkit\"4\n\x06Matrix\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x0c\n\x04rows\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ols\x18\x03 \x01(\x05\"e\n\x15MatrixAdditionRequest\x12%\n\x08matrix_a\x18\x01 \x01(\x0b\x32\x13.nla_toolkit.Matrix\x12%\n\x08matrix_b\x18\x02 \x01(\x0b\x32\x13.nla_toolkit.Matrix\"=\n\x16MatrixAdditionResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.nla_toolkit.Matrix\";\n\x14MatrixInverseRequest\x12#\n\x06matrix\x18\x01 \x01(\x0b\x32\x13.nla_toolkit.Matrix\"<\n\x15MatrixInverseResponse\x12#\n\x06result\x18\x01 \x01(\x0b\x32\x13.nla_toolkit.Matrix2\xd9\x01\n\x14LinearAlgebraService\x12`\n\x15PerformMatrixAddition\x12\".nla_toolkit.MatrixAdditionRequest\x1a#.nla_toolkit.MatrixAdditionResponse\x12_\n\x16PerformMatrixInversion\x12!.nla_toolkit.MatrixInverseRequest\x1a\".nla_toolkit.MatrixInverseResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nla_toolkit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MATRIX']._serialized_start=34
  _globals['_MATRIX']._serialized_end=86
  _globals['_MATRIXADDITIONREQUEST']._serialized_start=88
  _globals['_MATRIXADDITIONREQUEST']._serialized_end=189
  _globals['_MATRIXADDITIONRESPONSE']._serialized_start=191
  _globals['_MATRIXADDITIONRESPONSE']._serialized_end=252
  _globals['_MATRIXINVERSEREQUEST']._serialized_start=254
  _globals['_MATRIXINVERSEREQUEST']._serialized_end=313
  _globals['_MATRIXINVERSERESPONSE']._serialized_start=315
  _globals['_MATRIXINVERSERESPONSE']._serialized_end=375
  _globals['_LINEARALGEBRASERVICE']._serialized_start=378
  _globals['_LINEARALGEBRASERVICE']._serialized_end=595
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test-unary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10test-unary.proto\x12\x05unary\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08recieved\x18\x02 \x01(\x08\x32\x46\n\x05unary\x12=\n\x11GetServerResponse\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_unary_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=27
  _MESSAGE._serialized_end=53
  _MESSAGERESPONSE._serialized_start=55
  _MESSAGERESPONSE._serialized_end=107
  _UNARY._serialized_start=109
  _UNARY._serialized_end=179
# @@protoc_insertion_point(module_scope)
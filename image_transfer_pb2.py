# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14image_transfer.proto\x12\rimage_service\"#\n\rImageResponse\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\"#\n\x0cImageRequest\x12\x13\n\x0bvoidMessage\x18\x01 \x01(\t2X\n\rImageTransfer\x12G\n\x08getImage\x12\x1b.image_service.ImageRequest\x1a\x1c.image_service.ImageResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_transfer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_IMAGERESPONSE']._serialized_start=39
  _globals['_IMAGERESPONSE']._serialized_end=74
  _globals['_IMAGEREQUEST']._serialized_start=76
  _globals['_IMAGEREQUEST']._serialized_end=111
  _globals['_IMAGETRANSFER']._serialized_start=113
  _globals['_IMAGETRANSFER']._serialized_end=201
# @@protoc_insertion_point(module_scope)

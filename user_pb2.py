# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x07\n\x05\x45mpty\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"%\n\x08UserList\x12\x19\n\x05users\x18\x01 \x03(\x0b\x32\n.user.User2`\n\x0bUserService\x12+\n\x0cGetListUsers\x12\x0b.user.Empty\x1a\x0e.user.UserList\x12$\n\nCreateUser\x12\n.user.User\x1a\n.user.Userb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=20
  _globals['_EMPTY']._serialized_end=27
  _globals['_USER']._serialized_start=29
  _globals['_USER']._serialized_end=61
  _globals['_USERLIST']._serialized_start=63
  _globals['_USERLIST']._serialized_end=100
  _globals['_USERSERVICE']._serialized_start=102
  _globals['_USERSERVICE']._serialized_end=198
# @@protoc_insertion_point(module_scope)
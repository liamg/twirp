# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: importer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.twitchtv.twirp.internal.twirptest.importable import importable_pb2 as github_dot_com_dot_twitchtv_dot_twirp_dot_internal_dot_twirptest_dot_importable_dot_importable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='importer.proto',
  package='twirp.internal.twirptest.importer',
  syntax='proto3',
  serialized_options=_b('Z\010importer'),
  serialized_pb=_b('\n\x0eimporter.proto\x12!twirp.internal.twirptest.importer\x1aHgithub.com/twitchtv/twirp/internal/twirptest/importable/importable.proto2b\n\x04Svc2\x12Z\n\x04Send\x12(.twirp.internal.twirptest.importable.Msg\x1a(.twirp.internal.twirptest.importable.MsgB\nZ\x08importerb\x06proto3')
  ,
  dependencies=[github_dot_com_dot_twitchtv_dot_twirp_dot_internal_dot_twirptest_dot_importable_dot_importable__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SVC2 = _descriptor.ServiceDescriptor(
  name='Svc2',
  full_name='twirp.internal.twirptest.importer.Svc2',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=127,
  serialized_end=225,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='twirp.internal.twirptest.importer.Svc2.Send',
    index=0,
    containing_service=None,
    input_type=github_dot_com_dot_twitchtv_dot_twirp_dot_internal_dot_twirptest_dot_importable_dot_importable__pb2._MSG,
    output_type=github_dot_com_dot_twitchtv_dot_twirp_dot_internal_dot_twirptest_dot_importable_dot_importable__pb2._MSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC2)

DESCRIPTOR.services_by_name['Svc2'] = _SVC2

# @@protoc_insertion_point(module_scope)

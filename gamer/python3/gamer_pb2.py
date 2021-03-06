# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamer.proto',
  package='gamer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bgamer.proto\x12\x05gamer\"\x19\n\x0bPingMessage\x12\n\n\x02id\x18\x01 \x01(\t\"a\n\x0b\x41\x63tionInput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06gameId\x18\x02 \x01(\t\x12\x12\n\ntotalRound\x18\x03 \x01(\x05\x12\x14\n\x0c\x63urrentRound\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x05 \x03(\t\"(\n\x0c\x41\x63tionOutput\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t2n\n\x05Gamer\x12\x30\n\x04Ping\x12\x12.gamer.PingMessage\x1a\x12.gamer.PingMessage\"\x00\x12\x33\n\x06\x41\x63tion\x12\x12.gamer.ActionInput\x1a\x13.gamer.ActionOutput\"\x00\x62\x06proto3')
)




_PINGMESSAGE = _descriptor.Descriptor(
  name='PingMessage',
  full_name='gamer.PingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gamer.PingMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=47,
)


_ACTIONINPUT = _descriptor.Descriptor(
  name='ActionInput',
  full_name='gamer.ActionInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gamer.ActionInput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameId', full_name='gamer.ActionInput.gameId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalRound', full_name='gamer.ActionInput.totalRound', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentRound', full_name='gamer.ActionInput.currentRound', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gamer.ActionInput.data', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=146,
)


_ACTIONOUTPUT = _descriptor.Descriptor(
  name='ActionOutput',
  full_name='gamer.ActionOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gamer.ActionOutput.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gamer.ActionOutput.data', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['PingMessage'] = _PINGMESSAGE
DESCRIPTOR.message_types_by_name['ActionInput'] = _ACTIONINPUT
DESCRIPTOR.message_types_by_name['ActionOutput'] = _ACTIONOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingMessage = _reflection.GeneratedProtocolMessageType('PingMessage', (_message.Message,), dict(
  DESCRIPTOR = _PINGMESSAGE,
  __module__ = 'gamer_pb2'
  # @@protoc_insertion_point(class_scope:gamer.PingMessage)
  ))
_sym_db.RegisterMessage(PingMessage)

ActionInput = _reflection.GeneratedProtocolMessageType('ActionInput', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONINPUT,
  __module__ = 'gamer_pb2'
  # @@protoc_insertion_point(class_scope:gamer.ActionInput)
  ))
_sym_db.RegisterMessage(ActionInput)

ActionOutput = _reflection.GeneratedProtocolMessageType('ActionOutput', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONOUTPUT,
  __module__ = 'gamer_pb2'
  # @@protoc_insertion_point(class_scope:gamer.ActionOutput)
  ))
_sym_db.RegisterMessage(ActionOutput)



_GAMER = _descriptor.ServiceDescriptor(
  name='Gamer',
  full_name='gamer.Gamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=190,
  serialized_end=300,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='gamer.Gamer.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGMESSAGE,
    output_type=_PINGMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Action',
    full_name='gamer.Gamer.Action',
    index=1,
    containing_service=None,
    input_type=_ACTIONINPUT,
    output_type=_ACTIONOUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMER)

DESCRIPTOR.services_by_name['Gamer'] = _GAMER

# @@protoc_insertion_point(module_scope)

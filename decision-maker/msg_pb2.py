# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tmsg.proto\"\xce\x01\n\x07Request\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.Request.RequestType\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x01\x12\x1f\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x0f.Request.Config\x1a?\n\x06\x43onfig\x12\t\n\x01g\x18\x01 \x02(\x01\x12\t\n\x01k\x18\x02 \x02(\x01\x12\t\n\x01l\x18\x03 \x02(\x01\x12\t\n\x01m\x18\x04 \x02(\x01\x12\t\n\x01w\x18\x05 \x02(\x01\"-\n\x0bRequestType\x12\t\n\x05RESET\x10\x00\x12\x08\n\x04STEP\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\"\\\n\x08Response\x12\x1e\n\x05state\x18\x01 \x02(\x0b\x32\x0f.Response.State\x1a\x30\n\x05State\x12\r\n\x05\x61ngle\x18\x01 \x02(\x01\x12\x18\n\x10\x61ngular_velocity\x18\x02 \x02(\x01'
)



_REQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='Request.RequestType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STEP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=175,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_REQUEST_REQUESTTYPE)


_REQUEST_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Request.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='g', full_name='Request.Config.g', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k', full_name='Request.Config.k', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='l', full_name='Request.Config.l', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='m', full_name='Request.Config.m', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='Request.Config.w', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=173,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Request.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='Request.action', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='Request.config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_CONFIG, ],
  enum_types=[
    _REQUEST_REQUESTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=220,
)


_RESPONSE_STATE = _descriptor.Descriptor(
  name='State',
  full_name='Response.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='angle', full_name='Response.State.angle', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='Response.State.angular_velocity', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=314,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='Response.state', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_STATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=314,
)

_REQUEST_CONFIG.containing_type = _REQUEST
_REQUEST.fields_by_name['type'].enum_type = _REQUEST_REQUESTTYPE
_REQUEST.fields_by_name['config'].message_type = _REQUEST_CONFIG
_REQUEST_REQUESTTYPE.containing_type = _REQUEST
_RESPONSE_STATE.containing_type = _RESPONSE
_RESPONSE.fields_by_name['state'].message_type = _RESPONSE_STATE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'Config' : _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_CONFIG,
    '__module__' : 'msg_pb2'
    # @@protoc_insertion_point(class_scope:Request.Config)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.Config)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_STATE,
    '__module__' : 'msg_pb2'
    # @@protoc_insertion_point(class_scope:Response.State)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'msg_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.State)


# @@protoc_insertion_point(module_scope)

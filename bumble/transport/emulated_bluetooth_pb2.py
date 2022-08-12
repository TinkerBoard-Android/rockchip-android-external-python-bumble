# Copyright 2021-2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emulated_bluetooth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import emulated_bluetooth_packets_pb2 as emulated__bluetooth__packets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65mulated_bluetooth.proto\x12\x1b\x61ndroid.emulation.bluetooth\x1a emulated_bluetooth_packets.proto\"\x19\n\x07RawData\x12\x0e\n\x06packet\x18\x01 \x01(\x0c\x32\xcb\x02\n\x18\x45mulatedBluetoothService\x12\x64\n\x12registerClassicPhy\x12$.android.emulation.bluetooth.RawData\x1a$.android.emulation.bluetooth.RawData(\x01\x30\x01\x12`\n\x0eregisterBlePhy\x12$.android.emulation.bluetooth.RawData\x1a$.android.emulation.bluetooth.RawData(\x01\x30\x01\x12g\n\x11registerHCIDevice\x12&.android.emulation.bluetooth.HCIPacket\x1a&.android.emulation.bluetooth.HCIPacket(\x01\x30\x01\x42\"\n\x1e\x63om.android.emulator.bluetoothP\x01\x62\x06proto3')



_RAWDATA = DESCRIPTOR.message_types_by_name['RawData']
RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), {
  'DESCRIPTOR' : _RAWDATA,
  '__module__' : 'emulated_bluetooth_pb2'
  # @@protoc_insertion_point(class_scope:android.emulation.bluetooth.RawData)
  })
_sym_db.RegisterMessage(RawData)

_EMULATEDBLUETOOTHSERVICE = DESCRIPTOR.services_by_name['EmulatedBluetoothService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036com.android.emulator.bluetoothP\001'
  _RAWDATA._serialized_start=91
  _RAWDATA._serialized_end=116
  _EMULATEDBLUETOOTHSERVICE._serialized_start=119
  _EMULATEDBLUETOOTHSERVICE._serialized_end=450
# @@protoc_insertion_point(module_scope)

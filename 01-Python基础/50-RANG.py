import os
import serial
import time
import binascii
import zlib

# slot = 1
# slot_str = hex(slot)[2:].zfill(2)
# print slot_str

addr_bin = 12
addr_hex = hex(addr_bin)[2:].zfill(8)
print addr_hex
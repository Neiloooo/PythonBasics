a = "55 AA 01 00 2B 20 0C 01 55 55 55 55 FF FF FF FF FF FF FF FF FF FF FF FF 55 55 55 55 01 1A 09 0F 02 00 02 0B 0E 05 01 3C 00 03 02 FF FF FF FF FF 00 D9 "
b = "".join(a.split())

print b[16:-4]

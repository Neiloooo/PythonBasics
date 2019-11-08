# coding=utf-8
response = "4A8668005110"
esam = response[0:2]  # 交通运输部标识
print esam
districtCode = response[2:6]  # 8668 芯片商注册标识
print districtCode
esamId = response[6:10]  # OBU厂商标识
print esamId
COS = response[-4:]
print COS

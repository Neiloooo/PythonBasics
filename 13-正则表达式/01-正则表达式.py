# coding=utf-8
import re



def __checkBarCode(barCode):
    #必须16位
    if re.match("^[0-9]{16}$", barCode) == None:return False
    if not barCode.startswith("12345"):return False
    return True


print __checkBarCode("123456789012")
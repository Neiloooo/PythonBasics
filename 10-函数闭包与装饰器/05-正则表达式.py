# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re

s1 = "你a"
s2 = "12"
s4 = "a2"
s5 = "1A"
s6 = "11"

# 判断入参字符串是否是A-F,或0-9
an = re.compile("[a-fA-F0-9]")
match = an.findall(s6)
if len(match) == 2:
    print ("匹配成功")
else:
    print ("匹配失败")

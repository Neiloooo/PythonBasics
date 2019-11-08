# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 类似于一种参数的穿透,当然有自己的先用自己的
def father(fatherName, grandPa):
    def son():
        fatherName="不是李晓峰"
        print ('我的爸爸%s' % fatherName)

        def grandson():
            print ("我的爷爷是%s" % grandPa)

        grandson()

    son()


father("李晓峰", "李子")

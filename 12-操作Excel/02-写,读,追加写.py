# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import xlrd
import xlwt
from xlutils.copy import copy


# 创建excel并写入数据
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print(u"xls格式表格写入数据成功！")


# 向excel中追加数据
def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print(u"xls格式表格【追加】写入数据成功！")


# 读取excel
# def read_excel_xls(path):
#     workbook = xlrd.open_workbook(path)  # 打开工作簿
#     sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
#     worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
#     for i in range(0, worksheet.nrows):
#         for j in range(0, worksheet.ncols):
#             print(worksheet.cell_value(i, j), "\t")  # 逐行逐列读取数据
#         print()

# 创建表格所用方法
# 创建表所需参数
sheet_name_xls = u'测试专用表格'
value_title = [[u"镭雕条码", u"产品标识码", u"合同序列号"], ]
filename_or_stream = u"excel_test.xls"
# 创建表调用方法
write_excel_xls(filename_or_stream, sheet_name_xls, value_title)

# 追加表数据所需参数
# value2=[]00
while True:
    # 这里从input修改为raw_input
    a = raw_input("输入合同:")
    b = raw_input("输入mac:")
    c = raw_input("请输入雷蛇码:")
    filename_or_stream = 'excel_test.xls'
    if not a.strip() == "" and not b.strip() == "" and not c.strip() == "":
        value2 = [[a, b, c],  ]
        write_excel_xls_append(filename_or_stream, value2)
    else:
        print (u"有空别多想了")

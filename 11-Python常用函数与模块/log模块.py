# coding=utf-8
import logging


# --------basicConfig方式配置-------------------------
# 调整日志的参数
# logging.basicConfig(
#     # 调整日志级别
#     level=logging.DEBUG,
#     # 把日志放在其他的文件里,而不是放在控制台输出
#     # 如果需要存在别处,指定路径+文件名即可
#     filename="logger.log",
#     # 不会重复添加,会覆盖之前的日志信息
#     filemode="w",
#     # format格式化打印类型,参数为asctime只打印时间,行号,输出信息
#     format="%(asctime)s[%(lineno)d]%(message)s "
#
# )
#
# # 日志级别 默认warning级别
# # 参数是我们自己写的信息
# logging.debug('你好')
# logging.info('info message')

# ----------logger对象--------------------------------------------------------------
# 封装成一个函数可以供给外界调用
def logger():
    # 创建logger对象
    logger = logging.getLogger()
    # 调用logging的方法向文件里发送内容(日志)
    fh = logging.FileHandler("test_log")
    # 调用logging的方法向屏幕发送日志
    ch = logging.StreamHandler()

    # 自定义fm日志格式:(自定义日志格式)
    fm = logging.Formatter("%(asctime)s %(message)s")

    # 为fh和ch对象设置输出日志的格式
    fh.setFormatter(fm)
    ch.setFormatter(fm)
    # 设置logger属性_________________________________________________________________________
    # 将属性赋予logger对象,让他拥有向文件里发送日志的功能(类似java的配置类)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel("DEBUG")
    return logger


# ----------打印日志对象-------------------------------------------------------------------
# 创建函数接口
logger = logger()
# 打印日志信息:
logger.debug("你好啊")
logger.info("hello")
logger.warning("你好警告")
logger.error("你好错误")
# --------------------------------------------------------------------

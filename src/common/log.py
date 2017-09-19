import os

import time
import logging


class WriteLog(object):
    """记录日志工具类"""
    def __init__(self, logger_name=""):
        self.logger_name = logger_name
        self.runtime_path = "".join(["F:\AutoTestProject\WoLianTest\log", "Runtime.log"])
        self.error_path = "".join(["F:\AutoTestProject\WoLianTest\log", "Error.log"])
        if not os.path.exists("F:\AutoTestProject\WoLianTest\log"):
            os.makedirs("F:\AutoTestProject\WoLianTest\log")

    def add_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            #创建一个hander，用于写入日志文件
            fh = logging.FileHandler(self.runtime_path)
            fh.setLevel(logging.INFO)
            fh1 = logging.FileHandler(self.error_path)
            fh1.setLevel(logging.ERROR)

            fmt = "%(asctime)s [%(name)s-%(levelname)]:%(message)s"
            datefmt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            formatter = logging.Formatter(fmt, datefmt)
            fh.setFormatter(formatter)
            fh1.setFormatter(formatter)
            #给logger添加handler
            logger.addHandler(fh)
            logger.addHandler(fh1)
        return logger


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 13:49
# @Author  : Aries
# @Site    : 
# @File    : logs.py
# @Software: PyCharm
#!/usr/bin/env python
# 日志封装
import logging
import os
import time

class Log:
    def __init__(self):
        #获取项目主路径
        home_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # 获取存放日志的目录
        logs_path = os.path.join(home_path, 'file_logs')
        # 获取当前时间
        cur_time = time.strftime('%Y-%m-%d')
        # 创建日志文件
        self.file_name = os.path.join(logs_path,cur_time + '.log')
        # 创建日志收集器
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输出格式
        self.formatt = logging.Formatter('[%(asctime)s] - %(filename)s] - %(lineno)d - %(levelname)s: %(message)s')

    def get_log(self, level, masg):
        # 创建一个StreamHandler用于输出控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatt)
        self.logger.addHandler(sh)

        # 创建一个FileHandler用于输出文件
        fh = logging.FileHandler(self.file_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatt)
        self.logger.addHandler(fh)

        if level == 'INFO':
            self.logger.info(masg)
        elif level == 'DEBUG':
            self.logger.debug(masg)
        elif level == 'WARNING':
            self.logger.warning(masg)
        elif level == 'ERROR':
            self.logger.error(masg)
        elif level == 'CRITICAL':
            self.logger.critical(masg)

        # 移除重复日志
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        sh.close()
        fh.close()

    def log_info(self, masg):
        self.get_log('INFO', masg)

    def log_debug(self, masg):
        self.get_log('INFO', masg)

    def log_warning(self, masg):
        self.get_log('INFO', masg)

    def log_error(self, masg):
        self.get_log('INFO', masg)

    def log_critical(self, masg):
        self.get_log('INFO', masg)


if __name__ == '__main__':
    lg = Log()
    lg.log_info("准备测试")
    lg.log_debug("开始测试")
    lg.log_warning("测试进行中")

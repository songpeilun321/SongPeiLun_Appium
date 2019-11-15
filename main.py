#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 15:14
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharmto
#生成测试报告
import HTMLTestRunner
import time
import os
import unittest

#获取当前时间
cur_time = time.strftime("%Y-%m-%d %H-%M-%S")

#获取存放报告目录
home_path = os.path.abspath(os.path.dirname(__file__))
report_path = os.path.join(home_path,'report')

#用例路径
case_path = os.path.join(home_path,'case')

#加载测试用例
def all_case():
    disco = unittest.defaultTestLoader.discover(case_path,
                                        pattern='test_*.py',
                                        top_level_dir=None)
    return disco


if __name__ == '__main__':
    #报告存放路径
    html_path = os.path.join(report_path,cur_time+'.html')
    fp = open(html_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告')
    runner.run(all_case())
    fp.close()
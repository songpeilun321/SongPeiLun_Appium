#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 10:21
# @Author  : Aries
# @Site    : 
# @File    : operation_click.py
# @Software: PyCharm
#对元素进行操作
from test.login_page import LoginPage
import time

class Click_page:
    def __init__(self):
        self.lopage = LoginPage()


    def click_resource_file(self):
        time.sleep(2)
        self.lopage.get_page_resource_file_element().click()


if __name__ == '__main__':
    clpag = Click_page()
    clpag.click_resource_file()
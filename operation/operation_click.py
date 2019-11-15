#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 10:21
# @Author  : Aries
# @Site    : 
# @File    : operation_click.py
# @Software: PyCharm
#对元素进行操作
import time
from page.permission_page import LoginPage


class Click_page:
    def __init__(self):
        self.lopage = LoginPage()

    #操作文件元素
    def click_resource_file(self):
        time.sleep(2)
        self.lopage.get_page_resource_file_element().click()

    #操作通话元素元素
    def click_resource_iphone(self):
        time.sleep(2)
        self.lopage.get_page_resource_iphone_element().click()

    #操作软件协议同意元素
    def click_resource_consent(self):
        time.sleep(2)
        self.lopage.get_page_resource_consent_element().click()

    #操作密码登录元素
    def click_resource_login(self):
        time.sleep(2)
        self.lopage.get_page_resource_login_element().click()

    #操作点击登录密码
    def input_user_password(self,user,password):
        time.sleep(2)
        print(self.lopage.get_page_resource_input_phone_element().send_keys(user))
        print(self.lopage.get_page_resource_input_password_element().send_keys(password))

    #操作登录
    def click_resource_input_login(self):
        time.sleep(2)
        self.lopage.get_page_resource_input_login_element().click()


if __name__ == '__main__':
    clpag = Click_page()
    clpag.click_resource_file()
    clpag.click_resource_iphone()
    clpag.click_resource_consent()
    clpag.click_resource_login()
    clpag.input_user_password('137773987731','wqeqwea123456')
    clpag.click_resource_input_login()
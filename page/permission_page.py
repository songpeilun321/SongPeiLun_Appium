#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 19:02
# @Author  : Aries
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
#获取登录页面的元素信息

from devices.driver import Driver
from until.by_element import Element

class LoginPage:
    def __init__(self):
        driver = Driver()
        self.base_driver = driver.Android_driver()
        self.element = Element(self.base_driver)

    #获取文件元素信息
    def get_page_resource_file_element(self):
        return self.element.get_element('resource_file')

    #获取通话元素信息
    def get_page_resource_iphone_element(self):
        return self.element.get_element('resource_iphone')

    #获取软件协议同意元素信息
    def get_page_resource_consent_element(self):
        return self.element.get_element('resource_consent')

    #获取密码登录元素信息
    def get_page_resource_login_element(self):
        return self.element.get_element('resource_login')

    #获取输入账号元素信息
    def get_page_resource_input_phone_element(self):
        return self.element.get_element('resource_input_phone','login_element')

    #获取输入密码元素信息
    def get_page_resource_input_password_element(self):
        return self.element.get_element('resource_input_password','login_element')

    #获取登录信息
    def get_page_resource_input_login_element(self):
        return self.element.get_element('resource_input_login', 'login_element')


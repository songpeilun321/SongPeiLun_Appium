#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 13:49
# @Author  : Aries
# @Site    : 
# @File    : power_perform.py
# @Software: PyCharm
#执行元素的操作

from operation.power_click import Click_page

class Power_Perform:

    def __init__(self):
        self.clipag  = Click_page()

    #执行文件权限
    def power_resource_file(self):
        self.clipag.click_resource_file()

    #执通话权限
    def power_resource_iphone(self):
        self.clipag.click_resource_iphone()

    #执行协议权限
    def power_resource_consent(self):
        self.clipag.click_resource_consent()

    #执行密码登录
    def power_resource_login(self):
        self.clipag.click_resource_login()

    #输入账号密码
    def power_user_password(self):
        self.clipag.input_user_password('137773987731','wqeqwea123456')

    #执行登录
    def power_resource_input_login(self):
        self.clipag.click_resource_input_login()





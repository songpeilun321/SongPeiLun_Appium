#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 11:44
# @Author  : Aries
# @Site    : 
# @File    : test_driver.py
# @Software: PyCharm
from appium import webdriver
import os
import time

class Driver:
    def __init__(self):
        #获取apk的路径
        path_home = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.apk_path = os.path.join(path_home,'Android_apk','zhiliao.apk')

    def Android_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': '192.168.226.101:5555',#Genymotion模拟器
            # 'deviceName': '127.0.0.1:62001',       #夜神模拟器
            'app': self.apk_path,
            'appActivity': 'com.yyk.knowchat.group.welcome.WelcomeActivity'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(2)
        driver.find_element_by_id('com.yyk.knowchat:id/btnPositive').click()
        time.sleep(2)
        driver.find_element_by_id('com.yyk.knowchat:id/tv_password_login').click()
        time.sleep(2)
        driver.find_element_by_id('com.yyk.knowchat:id/et_input_phone').send_keys('137773987731')
        time.sleep(2)
        driver.find_element_by_id('com.yyk.knowchat:id/et_input_password').send_keys('wqeqwea123456')
        time.sleep(2)
        driver.find_element_by_id('com.yyk.knowchat:id/tv_sure_login').click()

if __name__ == '__main__':
    driver = Driver()
    driver.Android_driver()
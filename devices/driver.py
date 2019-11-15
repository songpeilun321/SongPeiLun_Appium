#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 14:23
# @Author  : Aries
# @Site    : 
# @File    : driver.py
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
        return driver

if __name__ == '__main__':
    driver = Driver()
    driver.Android_driver()


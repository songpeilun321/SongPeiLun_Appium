#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 15:50
# @Author  : Aries
# @Site    : 
# @File    : read_element.py
# 读取element配置文件
import configparser

class Read_Element:

    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'E:\Python_Appium\SongPeiLun_Appium\config\element.ini'
        else:
            self.file_path = file_path
        self.data = self.element_ini()

    #读取element配置文件
    def element_ini(self):
        cfg = configparser.ConfigParser()
        cfg.read(self.file_path,encoding='utf-8')
        return cfg

    #根据元素类型获取元素信息
    def get_value(self, key, vartest=None):
        if vartest == None:
            vartest = 'jurisdiction_element'
        try:
            value = self.data.get(vartest, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    rent = Read_Element()
    print(rent.get_value('resource_file'))

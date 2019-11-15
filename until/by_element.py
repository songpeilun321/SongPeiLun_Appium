#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 17:55
# @Author  : Aries
# @Site    : 
# @File    : by_element.py
# @Software: PyCharm
#定位元素信息的封装，元素类型和元素信息
from until.read_element import Read_Element

class Element:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key,value=None):
        read_element = Read_Element()
        local = read_element.get_value(key,value)

        if local !=None:
            by = local.split('>')[0]    #>前面的元素
            local_by = local.split('>')[1]     #>后面的元素
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'xpath':
                return  self.driver.find_element_by_xpath(local_by)
            elif by == 'classname':
                return self.driver.find_element_by_classname(local_by)
        else:
            return None

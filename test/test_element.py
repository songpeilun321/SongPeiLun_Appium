#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 9:58
# @Author  : Aries
# @Site    : 
# @File    : test_element.py
# @Software: PyCharm
from until.read_element import Read_Element

class Element:
    # def __init__(self,driver):
    #     self.driver = driver

    def get_element(self,key,value=None):
        read_element = Read_Element()
        local = read_element.get_value(key,value)
        # print(local)

        by = local.split('>')[0]    #>前面的元素
        local_by = local.split('>')[1]     #>后面的元素
        print(by)
        print(local_by)

        # if local !=None:
        #     by = local.split('>')[0]    #>前面的元素
        #     local_by = local.split('>')[1]     #>后面的元素
        #     if by == 'id':
        #         return self.driver.find_element_by_id(local_by)
        #     elif by == 'xpath':
        #         return  self.driver.find_element_by_xpath(local_by)
        #     elif by == 'classname':
        #         return self.driver.find_element_by_classname(local_by)
        # else:
        #     return None

if __name__ == '__main__':
    element = Element()
    element.get_element('resource_input_login','login_element')
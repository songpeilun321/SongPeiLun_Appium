#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 14:31
# @Author  : Aries
# @Site    : 
# @File    : test_power.py
# @Software: PyCharm
import unittest
from perform.power_perform import Power_Perform

class Power_Login(unittest.TestCase):

    def setUp(self):
        self.powper = Power_Perform()

    def test_run_porwer(self):
        self.powper.power_resource_file()
        self.powper.power_resource_iphone()
        self.powper.power_resource_consent()
        self.powper.power_resource_login()
        self.powper.power_user_password()
        self.powper.power_resource_input_login()

if __name__ == '__main__':
    unittest.main()

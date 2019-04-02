#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-02 15:39
# @Author  : Aries
# @Site    : 
# @File    : test_unittest.py
# @Software: PyCharm

import unittest
from demo import RunMain
class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        print('class 执行之前的方法')

    @classmethod
    def tearDownClass(cls):
        print('class 执行之后的方法')

    #每次方法前执行
    def setUp(self):
        self.run = RunMain()
        print('test-->setup')
    #每次方法后执行
    def tearDown(self):
        print('test-->teardown')

    def test_01(self):
        url = ''
        data = {

        }
        res = self.run.run_main(url,data)
        print('this is a testcase ')

    def test_02(self):
        url = ''
        data = {

        }
        res = self.run.run_main(url,data)
        print('this is a testcase2 ')

if __name__ == '__main__':
    unittest.main()
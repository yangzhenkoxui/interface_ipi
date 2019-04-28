#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 14:05
# @Author  : yangzhen
# @Site    : 
# @File    : run_test.py
# @Software: PyCharm

import sys
sys.path.append("")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DenpendentData
from util.send_email import SendEmail

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()

    #程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            request_data = self.data.get_data_for_json(i)
            expect = self.data.get_expect_data(i)
            header = self.data.is_header(i)
            depend_case = self.data.is_depend(i)
            if depend_case != None:
                self.depend_data = DenpendentData()
                #获取依赖相应数据
                depend_response_data = self.depend_data.get_data_for_key(i)
                #获取依赖的key
                depend_key = self.data.get_depend_field(i)
                request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, request_data, header)

            if is_run:
                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)
        print(len(pass_count))
        print(len(fail_count))
        self.send_mail.send_main(pass_count,fail_count)
if __name__ == '__main__':
    RunTest.go_on_run()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-08 15:30
# @Author  : yangzhen
# @Site    : 
# @File    : dependent_data.py
# @Software: PyCharm

from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse

class DenpendentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_execl = OperationExcel()
        self.getdata = GetData()

    #通过case_id去获取该case_id整行数据
    def get_case_line_data(self):
        rows_data = self.opera_execl.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row_num = self.opera_execl.get_row_num(self.case_id)
        request = self.getdata.get_data_for_json(row_num)
        header = self.getdata.is_header(row_num)
        method = self.getdata.get_request_data(row_num)
        url = self.getdata.get_request_url(row_num)
        res = run_method.run_main(method,url,request,header)
        return res

    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.getdata.get_dependent_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

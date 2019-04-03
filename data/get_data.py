#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 17:10
# @Author  : yangzhen
# @Site    : 
# @File    : get_data.py
# @Software: PyCharm
#获取Excel数据

from util.operation_excel import OperationExcel
import data_config
from util.operation_json import OperationJson

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    #去获取Excel行数，就是case的个数
    def get_case_lines(self):
        self.opera_excel.get_lines()


    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell_value(row,col)


    #是否携带header
    def is_header(self,row):
        col = data_config.get_header()
        header = self.opera_excel.get_cell_value(row,col)
        if header == 'yes':
            return data_config.get_data_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = data_config.get_run_way()
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取URL
    def get_request_url(self,row):
        col = data_config.get_url()
        request_url = self.opera_excel.get_cell_value(row,col)
        return request_url

    #获取请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    #通过获取关键字拿到data
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 16:54
# @Author  : yangzhen
# @Site    : 
# @File    : data_config.py
# @Software: PyCharm
#获取常量方法


class global_var:
    #case_id
    Id = '0'
    url = '1'
    run = '2'
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    data = '8'
    expect = '9'
    result = '10'

    #获取caseid
    def get_id(self):
        return global_var.Id

    def get_url(self):
        return global_var.url

    def get_run(self):
        return global_var.run

    def get_request_way(self):
        return global_var.request_way

    def get_header(self):
        return global_var.header

    def get_case_depend(self):
        return global_var.case_depend

    def get_data_depend(self):
        return global_var.data_depend

    def get_field_depend(self):
        return global_var.field_depend

    def get_data(self):
        return global_var.data

    def get_expect(self):
        return global_var.expect

    def get_result(self):
        return global_var.expect

    def get_header_value(self):
        header = {
            "header":"1234",
            "cookie":"yang"
        }
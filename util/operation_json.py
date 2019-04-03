#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 16:16
# @Author  : yangzhen
# @Site    : 
# @File    : operation_json.py
# @Software: PyCharm
#对json文件的操作

import json
class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
       with open('../data_config/login.json') as fp:
           data = json.load(fp)
           return data


    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('search'))
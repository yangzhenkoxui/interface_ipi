#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 14:55
# @Author  : yangzhen
# @Site    : 
# @File    : operation_excel.py
# @Software: PyCharm
#读取用例Excel文件类

import xlrd

class OperationExcel:
    def __init__(self,filename=None,sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = '../data_config/interface.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheet_by_index(self.sheet_id)
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
       return self.get_data().cell_value(row,col)



if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(0,0))

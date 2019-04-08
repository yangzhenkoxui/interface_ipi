#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 14:55
# @Author  : yangzhen
# @Site    : 
# @File    : operation_excel.py
# @Software: PyCharm
#读取用例Excel文件类

import xlrd
from xlutils.copy import copy

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

    #写入数据
    def write_value(self,row,col,value):
        '''
        写入Excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.filename)


    #根据对应的caseid找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols



if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cell_value(0,0))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-03 14:20
# @Author  : yangzhen
# @Site    : 
# @File    : mock_demo.py
# @Software: PyCharm

import mock

def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res
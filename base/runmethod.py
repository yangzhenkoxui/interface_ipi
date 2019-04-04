#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 13:31
# @Author  : yangzhen
# @Site    : 
# @File    : runmethod.py
# @Software: PyCharm
#封装的post，get基类
import requests

class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header).json()
        else:
            res = requests.get(url=url,data=data).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            self.post_main(url,data,header)
        else:
            self.get_main(url,data,header)

        return res
    
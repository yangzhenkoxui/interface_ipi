#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-04 13:31
# @Author  : yangzhen
# @Site    : 
# @File    : runmethod.py
# @Software: PyCharm
#封装的post，get基类
import requests
import json

class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            print(res.status_code)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url,data=data)
        return res.text

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            self.post_main(url,data,header)
        else:
            self.get_main(url,data,header)

        return json.dump(res,ensure_ascii=False,sort_keys=True,indent=2)
    
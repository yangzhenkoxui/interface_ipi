#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-02 15:37
# @Author  : Aries
# @Site    : 
# @File    : test_method.py
# @Software: PyCharm

import requests
import json

class RunMain:

    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dump(res,indent=2,sort_keys=True)


    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dump(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    url = ''
    data = {

    }
    run = RunMain(url,'GET',data)
    print run.res
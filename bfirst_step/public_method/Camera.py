import requests
import json
import os

class RunMain(object):

    #构造函数
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)
    def send_post(self,url, data):
        # post->get就是get接口的，但是上面的测试数据的是post请求，get没有测试
        res = requests.post(url=url, data=data).json()
        # 格式化json数据，indent=2是空格，sort是排序
        # return json.dumps(res, indent=2, sort_keys=True)
        return res
    def send_get(self,url, data):
        # post->get就是get接口的
        res = requests.get(url=url, params=data).json()
        # 格式化json数据，indent=2是空格，sort是排序
        # return json.dumps(res, indent=2, sort_keys=True)
        return res

    def run_main(self,url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res







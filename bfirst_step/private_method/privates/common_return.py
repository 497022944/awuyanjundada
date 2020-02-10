from bfirst_step.config.Log import *
from bfirst_step.config.LogBug import *
import re

logbug = LogBug()
logger = Log()

class common_return_value:
    @staticmethod
    def testxubao(self, StatusMessage):
        if StatusMessage == '续保成功':
            return True
        else:
            #logbug.debug("续保--异常信息为:{}".format(StatusMessage,))
            return False
    @staticmethod
    def testbaojia(self, baojiaStatusMessage):
        falg = True
        if baojiaStatusMessage == '请求发送成功':
            return falg
        else:
            #logbug.debug("报价--异常信息为:{}".format(baojiaStatusMessage))
            return

    @staticmethod
    def Offerresults(self, result):
        #results1 = re.findall('重复投保', results, re.S|re.M)
        if result == '获取报价信息成功':
            return True
        else:
            return False

    @staticmethod
    def Offer_the_results(self, results):
        results12 = str(results)
        results1 = re.findall('重复投保', results12, re.S|re.M)
        if results1 == ['重复投保']:
            return True
        else:
            return False

    @staticmethod
    def Offer_results(self, results1):
        results = str(results1)
        results2 = re.findall('同类型的险种', results, re.S|re.M)
        if results2 == ['同类型的险种']:
            return True
        else:
            return False
    # @staticmethod
    # def dict_get(dict1, objkey, default=None):
    #     for k, v in dict1.items():
    #         if k == objkey:
    #             return v
    #         else:
    #             if type(v) is dict:
    #                 ret = dict_get(v, objkey)
    #                 if ret is not default:
    #                     return ret

    @staticmethod
    def sum_insured(self, suminsured):
        baojiajg = suminsured
        BizTotal = baojiajg.res['Item']['BizTotal']#商业
        TaxTotal = baojiajg.res['Item']['TaxTotal']#车船
        ForceTotal = baojiajg.res['Item']['ForceTotal']#交强
        return BizTotal, TaxTotal, ForceTotal
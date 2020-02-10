import unittest
from bfirst_step.private_method.renewal_method.renewal_quotation_method import renewal_quotation

class Run_case(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01case(self, xianshangxianxia, xianshangdlr, xianxiadir, chengshi, gongshi, case, query_details_listna):
        # 实例请求方法
        renewal_quotations = renewal_quotation()
        # 获取请求返回得续保，报价参数
        quotation = renewal_quotations.quotation_method(xianshangxianxia, xianshangdlr, xianxiadir, chengshi, gongshi, case, query_details_listna)
        return quotation
if __name__ == '__main__':
    unittest.main()

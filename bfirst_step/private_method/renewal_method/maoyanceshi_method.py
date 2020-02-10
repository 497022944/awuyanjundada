import os
class Run_case:
    def __init__(self):
        # 初始化线上url
        self.xubaourl = 'http://it.91bihu.me/api/CarInsurance/getreinfo'
        self.baojiaurl = 'http://it.91bihu.me/api/CarInsurance/PostPrecisePrice'
        self.baojiajieguourl = 'http://it.91bihu.me/api/CarInsurance/GetPrecisePrice'
        # 初始化x线下url
        self.xubaourl = 'http://qa.interfaces.com/api/CarInsurance/getreinfo?'
        self.baojiaurl = 'http://qa.interfaces.com/api/CarInsurance/PostPrecisePrice?'
        self.baojiajieguourl = 'http://qa.interfaces.com/api/CarInsurance/GetPrecisePrice?'

    def test_01maoyan(self, xianshangdlr,xianxiadir,chengshi,gongshi):
        # 找车牌文件
        file_path = os.path.abspath(os.path.join(os.getcwd(), "./.")) + '\suplodfile\maoyanchepai.txt'
        # 打开文件
        file_open = open(file_path, 'r', encoding='utf-8-sig')
        # 加载文件
        licenseno_open = file_open.readlines()
        # 遍历车牌
        for licenseno in licenseno_open:
            licenseno = licenseno.strip('\n\t\w')
            url = self.xubaourl
            data = {
                'LicenseNo': licenseno,
                'CityCode': chengshi,
                'Agent': xianshangdlr,
                'Group': '1',
                'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                'SecCode': '23c73b3be4c698971dbf320699431545',
            }



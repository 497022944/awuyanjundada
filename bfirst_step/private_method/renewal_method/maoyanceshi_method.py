import os, time, json
from bfirst_step.public_method.Camera import RunMain
from bfirst_step.config.Log import Log
from bfirst_step.config.LogBug import LogBug
from bfirst_step.private_method.privates.common_return import common_return_value
from django.shortcuts import redirect
import os, datetime, time
from bfirst_step import views
logger = Log()
logbug = LogBug()
xianxiainfo = {}
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

    def test_01maoyan(self, xianshangdlr, xianxiadir, chengshi, gongshi):
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
                'Agent': xianxiadir,
                'Group': '1',
                'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                'SecCode': '23c73b3be4c698971dbf320699431545',
            }
            if len(licenseno) > 12 and len(licenseno) < 18:
                # 添加vin
                data['CarVin'] = data.pop('LicenseNo')
                # 耗时开始
                starttime = time.time()
                xubao = RunMain(url, 'GET', data)
                # 耗时结束
                endtime = time.time()
                # 耗时时间
                xubaovalues = float(endtime - starttime)
                # 获取续保结果
                xubaoreturn = xubao.res["StatusMessage"]
                xianxiainfo['续保结果'] = xubaoreturn
            elif len(licenseno) < 12:
                # 耗时开始
                starttime = time.time()
                xubao = RunMain(url, 'GET', data)
                # 耗时结束
                endtime = time.time()
                # 耗时时间
                xubaovalues = float(endtime - starttime)
                # 获取续保结果
                xubaoreturn = xubao.res["StatusMessage"]
                xianxiainfo['续保结果'] = xubaoreturn
            else:
                pass
            # 续保成功或取到车五项
            if xubaoreturn == '续保成功' or xubaoreturn == '获取车辆信息成功(车架号，发动机号，品牌型号及初登日期)，险种获取失败':
                # 商业到期时间
                NextBusinessStartDate1 = xubao.res['UserInfo']['NextBusinessStartDate']
                # 交强到期时间
                NextForceStartDate1 = xubao.res['UserInfo']['NextForceStartDate']
                LicenseOwner3 = xubao.res['UserInfo']['LicenseOwner']
                IdType3 = xubao.res['UserInfo']['IdType']
                CredentislasNum3 = xubao.res['UserInfo']['CredentislasNum']
                PostedName3 = xubao.res['UserInfo']['PostedName']
                HolderIdType3 = xubao.res['UserInfo']['HolderIdType']
                HolderIdCard3 = xubao.res['UserInfo']['HolderIdCard']
                InsuredName3 = xubao.res['UserInfo']['InsuredName']
                InsuredIdType3 = xubao.res['UserInfo']['InsuredIdType']
                InsuredIdCard3 = xubao.res['UserInfo']['InsuredIdCard']
                IsPublic = xubao.res['UserInfo']['IsPublic']
                personnel = {}
                personnel.update(LicenseOwner=LicenseOwner3, IdType=IdType3, CredentislasNum=CredentislasNum3,
                                 PostedName=PostedName3, HolderIdType=HolderIdType3, HolderIdCard=HolderIdCard3,
                                 InsuredName=InsuredName3, InsuredIdType=InsuredIdType3,
                                 InsuredIdCard=InsuredIdCard3)
                for k, item in personnel.items():
                    if IsPublic == 2:
                        if k == 'LicenseOwner':
                            if item == '' or item == 0:
                                personnel.update(LicenseOwner='叶星辰')
                            elif '*' in item:
                                personnel.update(LicenseOwner='叶星辰')
                        elif k == 'IdType':
                            if item == '' or item == 0:
                                personnel.update(IdType=1)
                        elif k == 'CredentislasNum':
                            if item == '' or item == 0:
                                personnel.update(CredentislasNum=430219198106274665)
                            elif '*' in item:
                                personnel.update(CredentislasNum=430219198106274665)
                        elif k == 'PostedName':
                            if item == '' or item == 0:
                                personnel.update(PostedName='叶星辰')
                            elif '*' in item:
                                personnel.update(PostedName='叶星辰')
                        elif k == 'HolderIdType':
                            if item == '' or item == 0:
                                personnel.update(HolderIdType=1)
                        elif k == 'HolderIdCard':
                            if item == '' or item == 0:
                                personnel.update(HolderIdCard=430219198106274665)
                            elif '*' in item:
                                personnel.update(HolderIdCard=430219198106274665)
                        elif k == 'InsuredName':
                            if item == '' or item == 0:
                                personnel.update(InsuredName='叶星辰')
                            elif '*' in item:
                                personnel.update(InsuredName='叶星辰')
                        elif k == 'InsuredIdType':
                            if item == '' or item == 0:
                                personnel.update(InsuredIdType=1)
                        elif k == 'InsuredIdCard':
                            if item == '' or item == 0:
                                personnel.update(InsuredIdCard=430219198106274665)
                            elif '*' in item:
                                personnel.update(InsuredIdCard=430219198106274665)
                        else:
                            pass
                    elif IsPublic == 1:
                        if k == 'LicenseOwner':
                            if item == '' or item == 0:
                                personnel.update(LicenseOwner='壁虎科技有限公司')
                            elif '*' in item:
                                personnel.update(LicenseOwner='壁虎科技有限公司')
                        elif k == 'IdType':
                            if item == '' or item == 0 or item == 1:
                                personnel.update(InsuredIdType=2)
                        elif k == 'CredentislasNum':
                            if item == '' or item == 0 or len(item) <= 15:
                                personnel.update(CredentislasNum=740054610)
                            elif '*' in item:
                                personnel.update(CredentislasNum=740054610)
                        elif k == 'PostedName':
                            if item == '' or item == 0:
                                personnel.update(PostedName='壁虎科技有限公司')
                            elif '*' in item:
                                personnel.update(PostedName='壁虎科技有限公司')
                        elif k == 'HolderIdType':
                            if item == '' or item == 0 or item == 1:
                                personnel.update(InsuredIdType=2)
                        elif k == 'HolderIdCard':
                            if item == '' or item == 0 or len(item) <= 15:
                                personnel.update(HolderIdCard=740054610)
                            elif '*' in item:
                                personnel.update(HolderIdCard=740054610)
                        elif k == 'InsuredName':
                            if item == '' or item == 0:
                                personnel.update(InsuredName='壁虎科技有限公司')
                            elif '*' in item:
                                personnel.update(InsuredName='壁虎科技有限公司')
                        elif k == 'InsuredIdType':
                            if item == '' or item == 0 or item == 1:
                                personnel.update(InsuredIdType=2)
                        elif k == 'InsuredIdCard':
                            if item == '' or item == 0 or len(item) <= 15:
                                personnel.update(InsuredIdCard=740054610)
                            elif '*' in item:
                                personnel.update(InsuredIdCard=740054610)
                        else:
                            pass
                    elif IsPublic == 0:
                        if k == 'LicenseOwner':
                            if item == '' or item == 0:
                                personnel.update(LicenseOwner='成紫风')
                            elif '*' in item:
                                personnel.update(LicenseOwner='成紫风')
                        elif k == 'IdType':
                            if item == '' or item == 0:
                                personnel.update(IdType=1)
                        elif k == 'CredentislasNum':
                            if item == '' or item == 0:
                                personnel.update(CredentislasNum=430219198106274665)
                            elif '*' in item:
                                personnel.update(CredentislasNum=430219198106274665)
                        elif k == 'PostedName':
                            if item == '' or item == 0:
                                personnel.update(PostedName='成紫风')
                            elif '*' in item:
                                personnel.update(PostedName='成紫风')
                        elif k == 'HolderIdType':
                            if item == '' or item == 0:
                                personnel.update(HolderIdType=1)
                        elif k == 'HolderIdCard':
                            if item == '' or item == 0:
                                personnel.update(HolderIdCard=430219198106274665)
                            elif '*' in item:
                                personnel.update(HolderIdCard=430219198106274665)
                        elif k == 'InsuredName':
                            if item == '' or item == 0:
                                personnel.update(InsuredName='成紫风')
                            elif '*' in item:
                                personnel.update(InsuredName='成紫风')
                        elif k == 'InsuredIdType':
                            if item == '' or item == 0:
                                personnel.update(InsuredIdType=1)
                        elif k == 'InsuredIdCard':
                            if item == '' or item == 0:
                                personnel.update(InsuredIdCard=430219198106274665)
                            elif '*' in item:
                                personnel.update(InsuredIdCard=430219198106274665)
                        else:
                            pass
                        # 报价请求
                url1 = self.baojiaurl
                data1 = {
                    'LicenseNo': xubao.res['UserInfo']['LicenseNo'],
                    'CityCode': chengshi,
                    'Agent': xianxiadir,
                    'CarOwnersName': personnel['LicenseOwner'],
                    'OwnerIdCardType': personnel['IdType'],
                    'IdCard': personnel['CredentislasNum'],
                    'InsuredName': personnel['PostedName'],
                    'InsuredIdType': personnel['HolderIdType'],
                    'InsuredIdCard': personnel['HolderIdCard'],
                    'HolderName': personnel['InsuredName'],
                    'HolderIdType': personnel['InsuredIdType'],
                    'HolderIdCard': personnel['InsuredIdCard'],
                    'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                    'SecCode': '23c73b3be4c698971dbf320699431545',
                    'QuoteGroup': gongshi,
                    'IsPublic': '0',
                    'SubmitGroup': '0',
                    'IsTempStorage': '1'
                }
                baojia = RunMain(url1, 'GET', data1)
                if baojia.res["StatusMessage"] == '请求发送成功':
                    time.sleep(30)  # 30秒报价请求获取
                    url2 = self.baojiajieguourl
                    data2 = {
                        'LicenseNo': xubao.res['UserInfo']['LicenseNo'],
                        'Agent': xianxiadir,
                        'CityCode': chengshi,
                        'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                        'SecCode': '23c73b3be4c698971dbf320699431545',
                        'QuoteGroup': gongshi,
                    }
                    baojiajg = RunMain(url2, 'GET', data2)

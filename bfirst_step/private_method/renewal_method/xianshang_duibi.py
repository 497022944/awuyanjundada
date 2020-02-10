import os, time, json
from django.shortcuts import render
from bfirst_step.public_method.Camera import RunMain
from bfirst_step.config.Log import Log
from bfirst_step.config.LogBug import LogBug
from bfirst_step.private_method.privates.common_return import common_return_value
from bfirst_step import views
logger = Log()
logbug = LogBug()
xianshangbaojiajieguo = {}
xianshangbaojiajieguo1 = {}
class runs_xianshang:
    def __init__(self):
        # 初始化续保utl
        self.xubaourl = 'http://it.91bihu.me/api/CarInsurance/getreinfo'
        self.baojiaurl = 'http://it.91bihu.me/api/CarInsurance/PostPrecisePrice'
        self.baojiajieguourl = 'http://it.91bihu.me/api/CarInsurance/GetPrecisePrice'

    # 线上请求
    def axianshang_duibi(self, xianshangdlr, chengshi, gongshi, case, query_details_listna):
        global xubaoreturn, xubao, NextForceStartDate1, NextBusinessStartDate1, NextForceStartDate, NextBusinessStartDate, cases, licenseno, duibishibai1, query_details

        # 存储返回值全局变量
        common_return = common_return_value()
        cases = case
        query_details = query_details_listna
        # 找车牌文件
        file_path = os.path.abspath(os.path.join(os.getcwd(), "./.")) + '\suplodfile\chepai.txt'
        # 打开文件
        file_open = open(file_path, 'r', encoding='utf-8-sig')
        # 加载文件
        licenseno_open = file_open.readlines()
        # 遍历车牌
        def dict_get(dict1, objkey, default=None):
            for k, v in dict1.items():
                if k == objkey:
                    return v
                else:
                    if type(v) is dict:
                        ret = dict_get(v, objkey)
                        if ret is not default:
                            return ret
        for licenseno in licenseno_open:
            licenseno = licenseno.strip('\n\t\w')
            xianshangbaojiajieguo[licenseno] = [licenseno]
            xianshangbaojiajieguo1.clear()
            url = self.xubaourl
            data = {
                'LicenseNo': licenseno,
                'CityCode': chengshi,
                'Agent': xianshangdlr,
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
                xianshangbaojiajieguo1['车牌'] = licenseno
                xianshangbaojiajieguo1['续保结果'] = xubaoreturn
                xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
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
                xianshangbaojiajieguo1['车牌'] = licenseno
                xianshangbaojiajieguo1['续保结果'] = xubaoreturn
                xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
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
                    'Agent': xianshangdlr,
                    'ForceTax': '1',
                    'IsPublic': '0',
                    'BuJiMianCheSun': '1',
                    'BuJiMianSanZhe': '1',
                    'SiJi': '10000',
                    'ChengKe': '10000',
                    'CheSun': '1',
                    'SanZhe': '500000',
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
                    'BuJiMianChengKe': '1',
                    'BuJiMianSiJi': '1',
                    'QuoteGroup': gongshi,
                    'SubmitGroup': '0',
                    'IsTempStorage': '1',
                }
                start = time.time()
                baojia = RunMain(url1, 'GET', data1)
                end = time.time()
                baojavalues = int(end - start)
                if baojia.res["StatusMessage"] == '请求发送成功':
                    time.sleep(30)  # 30秒报价请求获取
                    url2 = self.baojiajieguourl
                    data2 = {
                        'LicenseNo': xubao.res['UserInfo']['LicenseNo'],
                        'Agent': xianshangdlr,
                        'CityCode': chengshi,
                        'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                        'SecCode': '23c73b3be4c698971dbf320699431545',
                        'QuoteGroup': gongshi,
                    }
                    baojiajg = RunMain(url2, 'GET', data2)
                    xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
                    Offer_results1 = baojiajg.res["StatusMessage"]
                    xianshangbaojiajieguo1['报价请求结果'] = Offer_results1
                    if Offer_results1 == '获取报价信息成功':
                        QuoteResultt = baojiajg.res['Item']['QuoteResult']
                        QuoteResultt1 = baojiajg.res['Item']['QuoteStatus']
                        xianshangbaojiajieguo1['报价获取结果'] = QuoteResultt
                        xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
                        Repeat_insurance = common_return.Offer_the_results(self, QuoteResultt)
                        the_same = common_return.Offer_results(self, QuoteResultt)
                        BizTotal = baojiajg.res['Item']['BizTotal']  # 商业
                        TaxTotal = baojiajg.res['Item']['TaxTotal']  # 车船
                        ForceTotal = baojiajg.res['Item']['ForceTotal']  # 交强
                        CheSun = dict_get(baojiajg.res, 'CheSun')
                        CheSunBjm = dict_get(baojiajg.res, 'BuJiMianCheSun')
                        SanZhe = dict_get(baojiajg.res, 'SanZhe')
                        SanZheBjm = dict_get(baojiajg.res, 'BuJiMianSanZhe')
                        SiJi = dict_get(baojiajg.res, 'SiJi')
                        SiJiBjm = dict_get(baojiajg.res, 'BuJiMianSiJi')
                        ChengKe = dict_get(baojiajg.res, 'ChengKe')
                        ChengKeBjm = dict_get(baojiajg.res, 'BuJiMianChengKe')
                        ##QuoteStatuss报价状态，-1=未报价， 0=报价失败，>0报价成功
                        if QuoteResultt1 <= 0:
                            if Repeat_insurance == True:
                                xianshangbaojiajieguo1['商业'] = str(BizTotal)
                                xianshangbaojiajieguo1['交强'] = str(ForceTotal)
                                xianshangbaojiajieguo1['车船'] = str(TaxTotal)
                                xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
                            elif the_same == True:
                                xianshangbaojiajieguo1['商业'] = str(BizTotal)
                                xianshangbaojiajieguo1['交强'] = str(ForceTotal)
                                xianshangbaojiajieguo1['车船'] = str(TaxTotal)
                                xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
                            else:
                                xianshangbaojiajieguo1['商业'] = str(BizTotal)
                                xianshangbaojiajieguo1['交强'] = str(ForceTotal)
                                xianshangbaojiajieguo1['车船'] = str(TaxTotal)
                                xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()
                        else:
                            xianshangbaojiajieguo1['商业'] = str(BizTotal)
                            xianshangbaojiajieguo1['交强'] = str(ForceTotal)
                            xianshangbaojiajieguo1['车船'] = str(TaxTotal)
                            xianshangbaojiajieguo[licenseno] = xianshangbaojiajieguo1.copy()


                    else:
                        logbug.debug("获取报价信息失败：车牌--{}".format(licenseno))

                else:
                    logbug.debug("请求失败：车牌--{}".format(licenseno))

            else:
                logbug.debug("续保失败：车牌--{}".format(licenseno))
        return xianshangbaojiajieguo
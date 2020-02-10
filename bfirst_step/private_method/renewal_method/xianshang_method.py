import os, time, json
from bfirst_step.public_method.Camera import RunMain
from bfirst_step.config.Log import Log
from bfirst_step.config.LogBug import LogBug
from bfirst_step.private_method.privates.common_return import common_return_value
from bfirst_step import views
logger = Log()
logbug = LogBug()
xianxiainfo = {}
class run_xianshang:
    def __init__(self):
        # 初始化续保utl
        self.xubaourl = 'http://it.91bihu.me/api/CarInsurance/getreinfo'
        self.baojiaurl = 'http://it.91bihu.me/api/CarInsurance/PostPrecisePrice'
        self.baojiajieguourl = 'http://it.91bihu.me/api/CarInsurance/GetPrecisePrice'

    def pichuli(self, Selectthe):
        global datas, Selecttheusec, NextForceStartDate, NextBusinessStartDate
        Select = cases.split(',')
        if NextForceStartDate1 == '':
            NextForceStartDate = time.strftime('%Y-%m-%d')
        else:
            NextForceStartDate = NextForceStartDate1
        if NextBusinessStartDate1 == '':
            NextBusinessStartDate = time.strftime('%Y-%m-%d')
        elif NextBusinessStartDate1 != '':
            NextBusinessStartDate = NextBusinessStartDate1
        for Selecttheusec in Select:
            # 单交强
            if Selecttheusec == '1' and Selectthe == '1':
                datas = {
                    'ForceTax': '2',
                    'ForceStartDate': NextForceStartDate,
                }
                jiao = '交强险'
                xianxiainfo['请求用例'] = jiao
            # 单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+不计免赔）
            elif Selecttheusec == '2' and Selectthe == '2':
                datas = {
                    'ForceTax': '0',
                    'CheSun': '1',
                    'BuJiMianCheSun': '1',
                    'SanZhe': '500000',
                    'BuJiMianSanZhe': '1',
                    'SiJi': '2000',
                    'BuJiMianSiJi': '1',
                    'ChengKe': '2000',
                    'BuJiMianChengKe': '1',
                    'DaoQiang': '1',
                    'BuJiMianDaoQiang': '1',
                    'BizStartDate': NextBusinessStartDate,

                }
                jiao = '单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）（无不计免赔））
            elif Selecttheusec == '3' and Selectthe == '3':
                datas = {
                    'ForceTax': '0',
                    'CheSun': '1',
                    'SanZhe': '500000',
                    'SiJi': '2000',
                    'ChengKe': '2000',
                    'DaoQiang': '1',
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）（无不计免赔））'
                xianxiainfo['请求用例'] = jiao
            # 单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)）+不计免赔）
            elif Selecttheusec == '4' and Selectthe == '4':
                datas = {
                    'ForceTax': '0',
                    'CheSun': '1',
                    'BuJiMianCheSun': '1',
                    'SanZhe': '500000',
                    'BuJiMianSanZhe': '1',
                    'SiJi': '2000',
                    'BuJiMianSiJi': '1',
                    'ChengKe': '2000',
                    'BuJiMianChengKe': '1',
                    'DaoQiang': '1',
                    'BuJiMianDaoQiang': '1',
                    'HuaHen': '2000',
                    'BuJiMianHuaHen': '1',
                    'BoLi': '1',
                    'ZiRan': '1',
                    'BuJiMianZiRan': '1',
                    'SheShui': '1',
                    'BuJiMianSheShui': '1',
                    'HcSanFangTeYue': '1',
                    'HcXiuLiChangType': '0',
                    'HcXiuLiChang': '0.3',
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)）+不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 单商业  单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃、自燃损失、涉水、车损无发找第三方、指定修理厂）（无不计免赔））
            elif Selecttheusec == '5' and Selectthe == '5':
                datas = {
                    'ForceTax': '0',
                    'CheSun': '1',
                    'SanZhe': '500000',
                    'SiJi': '2000',
                    'ChengKe': '2000',
                    'DaoQiang': '1',
                    'HuaHen': '2000',
                    'BoLi': '1',
                    'ZiRan': '1',
                    'SheShui': '1',
                    'HcSanFangTeYue': '1',
                    'HcXiuLiChangType': '0',
                    'HcXiuLiChang': '0.3',
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)）无不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）+不计免赔）
            elif Selecttheusec == '6' and Selectthe == '6':
                datas = {
                    'ForceTax': '1',
                    'CheSun': '1',
                    'BuJiMianCheSun': '1',
                    'SanZhe': '500000',
                    'BuJiMianSanZhe': '1',
                    'SiJi': '2000',
                    'BuJiMianSiJi': '1',
                    'ChengKe': '2000',
                    'BuJiMianChengKe': '1',
                    'DaoQiang': '1',
                    'BuJiMianDaoQiang': '1',
                    'HcXiuLiChang': '0.3',
                    'ForceStartDate': NextForceStartDate,
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）+不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）（无不计免赔））
            elif Selecttheusec == '7' and Selectthe == '7':
                datas = {
                    'ForceTax': '1',
                    'CheSun': '1',
                    'SanZhe': '500000',
                    'SiJi': '2000',
                    'ChengKe': '2000',
                    'DaoQiang': '1',
                    'ForceStartDate': NextForceStartDate,
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）（无不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)）+不计免赔）
            elif Selecttheusec == '8' and Selectthe == '8':
                datas = {
                    'ForceTax': '1',
                    'CheSun': '1',
                    'BuJiMianCheSun': '1',
                    'SanZhe': '500000',
                    'BuJiMianSanZhe': '1',
                    'SiJi': '2000',
                    'BuJiMianSiJi': '1',
                    'ChengKe': '2000',
                    'BuJiMianChengKe': '1',
                    'DaoQiang': '1',
                    'BuJiMianDaoQiang': '1',
                    'HuaHen': '2000',
                    'BuJiMianHuaHen': '1',
                    'BoLi': '1',
                    'ZiRan': '1',
                    'BuJiMianZiRan': '1',
                    'SheShui': '1',
                    'BuJiMianSheShui': '1',
                    'HcSanFangTeYue': '1',
                    'HcXiuLiChangType': '0',
                    'HcXiuLiChang': '0.3',
                    'ForceStartDate': NextForceStartDate,
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)）+不计免赔）'
                xianxiainfo['请求用例'] = jiao
            # 双险种  单商业  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃、自燃损失、涉水、车损无发找第三方、指定修理厂）（无不计免赔））
            elif Selecttheusec == '9' and Selectthe == '9':
                datas = {
                    'ForceTax': '1',
                    'CheSun': '1',
                    'SanZhe': '500000',
                    'SiJi': '2000',
                    'ChengKe': '2000',
                    'DaoQiang': '1',
                    'HuaHen': '2000',
                    'BoLi': '1',
                    'ZiRan': '1',
                    'SheShui': '1',
                    'HcSanFangTeYue': '1',
                    'HcXiuLiChang': '0.3',
                    'HcXiuLiChangType': '0',
                    'ForceStartDate': NextForceStartDate,
                    'BizStartDate': NextBusinessStartDate,
                }
                jiao = '双险种  （基本险（车损、三者、司机座位、乘客座位、盗抢）+附加险（划痕、玻璃(国产)、自燃损失、涉水、车损无发找第三方、指定修理厂(国产)无不计免赔）'
                xianxiainfo['请求用例'] = jiao
            else:
                pass
        return datas

    def baojiareturn(self, pichu, data, licenseNO):
        duibizhanshi = {}
        duibishibai = {}
        rizhibaojiaduibi = {}
        datas = {}
        datas.update(data)
        duibizhanshi.clear()
        duibishibai.clear()
        if pichu == '1':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'BizTotal':
                                if v1 == 0:
                                    duibizhanshi[k1] = v1
                                else:
                                    duibishibai[k1] = v1
                            elif k1 == 'ForceTotal':
                                if v1 != 0:
                                    duibizhanshi[k1] = v1
                                else:
                                    duibishibai[k1] = v1
                            elif k1 == 'TaxTotal':
                                if v1 == 0 or v1 != 0:
                                    duibizhanshi[k1] = v1
                                else:
                                    duibishibai[k1] = v1
            for k, v in datas.items():
                if k == 'QuoteStatus':
                    if k == 'QuoteStatus' and v <= 0:
                        duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                        dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True, indent=2)
                        logbug.debug(
                            "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'], dictnews))
                        duibijieguoshi = '无'
                        baoebaofeiduibi = '失败'
                        views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                           duibishibai1['续保结果'], duibishibai1['报价状态'], duibishibai1['请求用例id'],
                                           dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                    else:
                        duibichenggong = dict(duibizhanshi, **xianxiainfo)
                        dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True, indent=2)
                        logger.info(
                            "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'], dictnews))
                        duibijieguoshi = '无'
                        baoebaofeiduibi = '成功'
                        views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                           duibichenggong['续保结果'], duibichenggong['报价状态'], duibichenggong['请求用例id'],
                                           dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '2':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianCheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianDaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '3':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '4':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianCheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianDaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianHuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcXiuLiChang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcSanFangTeYue':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '5':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcXiuLiChang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcSanFangTeYue':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '6':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianCheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianDaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    for kcs, vcs in v1.items():
                                        if kcs == 'BaoE' and vcs == 0:
                                            duibishibai[k1] = v1
                                            for kcs1, vcs1 in v1.items():
                                                if kcs1 == 'BaoFei' and vcs1 != 0:
                                                    duibishibai[k1] = v1
                                        elif kcs == 'BaoE' and vcs != 0:
                                            duibizhanshi[k1] = v1
                                            for kcs1, vcs1 in v1.items():
                                                if kcs1 == 'BaoFei' and vcs1 == 0:
                                                    duibishibai[k1] = v1
                                                elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                    duibizhanshi[k1] = v1
                                        elif kcs == 'BaoFei' and vcs == 0:
                                            duibishibai[k1] = v1
                                            for kcs1, vcs1 in v1.items():
                                                if kcs1 == 'BaoE' and vcs1 != 0:
                                                    duibishibai[k1] = v1
                                        elif kcs == 'BaoFei' and vcs != 0:
                                            duibizhanshi[k1] = v1
                                            for kcs1, vcs1 in v1.items():
                                                if kcs1 == 'BaoE' and vcs1 == 0:
                                                    duibishibai[k1] = v1
                                                elif kcs1 == 'BaoE' and vcs1 != 0:
                                                    duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '7':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '8':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianCheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianDaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianHuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianSheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'BuJiMianZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcXiuLiChang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcSanFangTeYue':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)

        elif pichu == '9':
            for k, v in datas.items():
                if k == 'QuoteResult':
                    ks = common_return_value.Offer_the_results(self, datas[k])
                    if ks == True:
                        pass
                    else:
                        for k1, v1 in datas.items():
                            if k1 == 'CheSun':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SanZhe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'DaoQiang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SiJi':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ChengKe':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HuaHen':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'SheShui':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'ZiRan':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcXiuLiChang':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                            elif k1 == 'HcSanFangTeYue':
                                for kcs, vcs in v1.items():
                                    if kcs == 'BaoE' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoE' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoFei' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoFei' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                                    elif kcs == 'BaoFei' and vcs == 0:
                                        duibishibai[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 != 0:
                                                duibishibai[k1] = v1
                                    elif kcs == 'BaoFei' and vcs != 0:
                                        duibizhanshi[k1] = v1
                                        for kcs1, vcs1 in v1.items():
                                            if kcs1 == 'BaoE' and vcs1 == 0:
                                                duibishibai[k1] = v1
                                            elif kcs1 == 'BaoE' and vcs1 != 0:
                                                duibizhanshi[k1] = v1
                        for k, v in datas.items():
                            if k == 'QuoteStatus':
                                if k == 'QuoteStatus' and v <= 0:
                                    duibishibai1 = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibishibai1, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logbug.debug(
                                        "日志记录--险种对比失败---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '失败'
                                    views.details_data(licenseno, duibishibai1['保险公司'], duibishibai1['报价城市'],
                                                       duibishibai1['续保结果'], duibishibai1['报价状态'],
                                                       duibishibai1['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
                                else:
                                    duibichenggong = dict(duibizhanshi, **xianxiainfo)
                                    dictnews = json.dumps(duibichenggong, ensure_ascii=False, sort_keys=True,
                                                          indent=2)
                                    logger.info(
                                        "日志记录--险种对比成功---{}--{}--{}".format(licenseNO, xianxiainfo['请求用例'],
                                                                           dictnews))
                                    duibijieguoshi = '无'
                                    baoebaofeiduibi = '成功'
                                    views.details_data(licenseno, duibichenggong['保险公司'], duibichenggong['报价城市'],
                                                       duibichenggong['续保结果'], duibichenggong['报价状态'],
                                                       duibichenggong['请求用例id'],
                                                       dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
        else:
            logbug.debug("日志记录--case为:{}---不存在".format(pichu))

        return xianxiainfo

    def rizhibaojia(self):
        if '报价耗时' in xianxiainfo:
            del xianxiainfo['报价耗时']
        if '报价请求' in xianxiainfo:
            del xianxiainfo['报价请求']
        if '商业' in xianxiainfo:
            del xianxiainfo['商业']
        if '交强' in xianxiainfo:
            del xianxiainfo['交强']
        if '车船' in xianxiainfo:
            del xianxiainfo['车船']
        if '请求用例' in xianxiainfo:
            del xianxiainfo['请求用例']
        if '请求用例id' in xianxiainfo:
            del xianxiainfo['请求用例id']
        if '获取结果' in xianxiainfo:
            del xianxiainfo['获取结果']
        if '商业起保时间' in xianxiainfo:
            del xianxiainfo['商业起保时间']
        if '交强起保时间' in xianxiainfo:
            del xianxiainfo['交强起保时间']
        if '保险公司' in xianxiainfo:
            del xianxiainfo['保险公司']

    def rizhixubao(self):
        dictnews = json.dumps(xianxiainfo, ensure_ascii=False, sort_keys=True, indent=2)
        logbug.debug("日志记录--{}--{}".format(licenseno, dictnews))
        duibijieguoshi = '无'
        baoebaofeiduibi = '失败'
        Insurance = '0'
        offer = '报价失败'
        sceneid = '0'
        details = '0'
        baojiachengshi = '0'
        views.details_data(licenseno, Insurance, baojiachengshi, xianxiainfo['续保结果'], offer, sceneid, dictnews,
                           duibijieguoshi, baoebaofeiduibi, query_details)
        return xianxiainfo

    def rizhibaojiashibai(self):
        try:
            dictnews = json.dumps(xianxiainfo, ensure_ascii=False, sort_keys=True, indent=2)
            duibijieguoshi = '无'
            baoebaofeiduibi = '失败'
            offer = '报价失败'
            details = '0'
            views.details_data(licenseno, xianxiainfo['保险公司'], xianxiainfo['报价城市'], xianxiainfo['续保结果'], offer,
                               xianxiainfo['请求用例id'], dictnews, duibijieguoshi, baoebaofeiduibi, query_details)
            return xianxiainfo
        except Exception:
            return xianxiainfo
    # 线上请求
    def axianshang_methods(self,xianshangdlr, chengshi, gongshi, case, query_details_listna):
        global xubaoreturn, xubao, NextForceStartDate1, NextBusinessStartDate1, NextForceStartDate, NextBusinessStartDate, cases, licenseno, duibishibai1, query_details

        #存储返回值全局变量
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
                    'Agent': xianshangdlr,
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
                Select = cases.split(',')
                for Selecttheusec in Select:
                    xianxiainfo['请求用例id'] = Selecttheusec
                    xianxiainfo['请求用例'] = Selecttheusec
                    pichulis = run_xianshang.pichuli(self, Selecttheusec)
                    # 线上 单交强 当Selecttheusec = ‘1’得时候自动请求交强
                    hebingdict = dict(pichulis, **data1)
                    print(hebingdict)
                    start = time.time()
                    baojia = RunMain(url1, 'GET', hebingdict)
                    end = time.time()
                    baojavalues = float(end - start)
                    baojava = round(baojavalues)
                    print(xianxiainfo)
                    xianxiainfo['保险公司'] = gongshi
                    xianxiainfo['报价城市'] = chengshi
                    xianxiainfo['报价耗时'] = baojava
                    xianxiainfo['报价请求'] = baojia.res["StatusMessage"]
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
                        print(baojiajg.res['Item']['QuoteStatus'])
                        if baojiajg.res['Item']['QuoteStatus'] == 0:
                            xianxiainfo['报价状态'] = '报价失败'
                        elif baojiajg.res['Item']['QuoteStatus'] == -1:
                            xianxiainfo['报价状态'] = '未报价'
                        else:
                            xianxiainfo['报价状态'] = '报价成功'
                        xianxiainfo['获取结果'] = baojiajg.res['Item']['QuoteResult']
                        Offer_results1 = baojiajg.res["StatusMessage"]
                        if Offer_results1 == '获取报价信息成功':
                            QuoteResultt = baojiajg.res['Item']['QuoteResult']
                            QuoteResultt1 = baojiajg.res['Item']['QuoteStatus']
                            Repeat_insurance = common_return.Offer_the_results(self, QuoteResultt)
                            the_same = common_return.Offer_results(self, QuoteResultt)
                            xianxiainfo['商业起保时间'] = baojiajg.res['UserInfo']['BusinessStartDate']
                            xianxiainfo['交强起保时间'] = baojiajg.res['UserInfo']['ForceStartDate']
                            xianxiainfo['商业'] = baojiajg.res['Item']['BizTotal']  # 商业
                            xianxiainfo['交强'] = baojiajg.res['Item']['ForceTotal']  # 交强
                            xianxiainfo['车船'] = baojiajg.res['Item']['TaxTotal']  # 车船
                            if QuoteResultt1 > 0:
                                if Repeat_insurance == True:

                                    run_xianshang.baojiareturn(self, Selecttheusec, baojiajg.res['Item'],
                                                                 licenseno)
                                    Xianshang_dandu1 = run_xianshang()
                                    Xianshang_dandu1.rizhibaojia()
                                    baojiajg.res.clear()
                                    continue
                                elif the_same == True:
                                    run_xianshang.baojiareturn(self, Selecttheusec, baojiajg.res['Item'],
                                                                 licenseno)
                                    Xianshang_dandu1 = run_xianshang()
                                    Xianshang_dandu1.rizhibaojia()
                                    baojiajg.res.clear()
                                    continue
                                else:
                                    run_xianshang.baojiareturn(self, Selecttheusec, baojiajg.res['Item'],
                                                                 licenseno)
                                    Xianshang_dandu1 = run_xianshang()
                                    Xianshang_dandu1.rizhibaojia()
                                    baojiajg.res.clear()
                                    continue
                            else:
                                # 报价信息返回并与case处理
                                run_xianshang.baojiareturn(self, Selecttheusec, baojiajg.res['Item'],
                                                             licenseno)
                                Xianshang_dandu1 = run_xianshang()
                                Xianshang_dandu1.rizhibaojia()
                                baojiajg.res.clear()
                                continue

                        # 获取报价结果失败
                        else:
                            Xianshang_dandu1 = run_xianshang()
                            Xianshang_dandu1.rizhibaojia()
                            run_xianshang.baojiareturn(self, Selecttheusec, baojiajg.res['Item'], licenseno)
                            continue
                    # 请求发送失败
                    else:
                        Xianshang_dandu1 = run_xianshang()
                        Xianshang_dandu1.rizhibaojiashibai()
                        continue

            # 续保失败
            else:
                Xianshang_dandu1 = run_xianshang()
                Xianshang_dandu1.rizhixubao()
                continue



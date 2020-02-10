from bfirst_step.config.Log import Log
from bfirst_step.config.LogBug import LogBug
from bfirst_step.public_method.Camera import RunMain
from bfirst_step.private_method.renewal_method.xianshang_method import run_xianshang
from bfirst_step.private_method.renewal_method.xianxia_method import run_xianxia
from bfirst_step.private_method.renewal_method.xianxia_duibi import runs_xianxia
from bfirst_step.private_method.renewal_method.xianshang_duibi import runs_xianshang
import os,json
from bfirst_step import views

logger = Log()
logbug = LogBug()

# 线上线下对比存储并且分类
jsondict = {
    '失败': {
        '线上对比失败': {},
        '线下对比失败': {}
    }
}
jsondict1 = {
    '成功': {
        '线上对比成功': {},
        '线下对比成功': {}
    }
}
jsondictxianshang = {}
jsondictxianxia = {}
jsondictchenggongx = {}
jsondictshibaix = {}
duibikey = []
xianshang = {}
xianxia = {}
keyfuzhi = []
class renewal_quotation:
    # 续保报价请求方法
    def quotation_method(self, xianshangxianxia, xianshangdlr, xianxiadir, chengshi, gongshi, case, query_details_listna):
        global duibi
        # 找车牌文件
        file_path = os.path.abspath(os.path.join(os.getcwd(), "./.")) + '\suplodfile\chepai.txt'
        # 打开文件
        file_open = open(file_path, 'r', encoding='utf-8-sig')
        # 加载文件
        licenseno_open = file_open.readlines()
        #判断线上线下或对比
        if xianshangxianxia == '1':
            run_xianshangs = run_xianshang()
            mehtod_xianshang = run_xianshangs.axianshang_methods(xianshangdlr, chengshi, gongshi, case, query_details_listna)
            listni = run_xianshang.rizhibaojiashibai(self)
            return listni
        elif xianshangxianxia == '2':
            run_xianxias = run_xianxia()
            mehtod_xianshang = run_xianxias.axianxia_methods(xianxiadir, chengshi, gongshi, case,query_details_listna)
            listni = run_xianxia.rizhibaojiashibai(self)
            return listni
        else:
            xianxia_names = runs_xianxia()
            xianxiadict = xianxia_names.axianxia_duibi(xianxiadir, chengshi, gongshi, case, query_details_listna)
            xianshang_names = runs_xianshang()
            xianshangdict = xianshang_names.axianshang_duibi(xianshangdlr, chengshi, gongshi, case, query_details_listna)
            for k, v in xianshangdict.items():
                for k1, v1 in xianxiadict.items():
                    if k == k1:
                        jsondict1['成功']['线上对比成功'] = {}
                        jsondict1['成功']['线下对比成功'] = {}
                        jsondict['失败']['线上对比失败'] = {}
                        jsondict['失败']['线下对比失败'] = {}
                        keyfuzhi.clear()
                        for k2, v2 in v.items():
                            keyfuzhi.append(k2)
                        for key in keyfuzhi:
                            jsondictxianshang.clear()
                            jsondictxianxia.clear()
                            if key in v and key in v1 and v[key] in v1[key]:
                                jsondictxianshang[key] = v[key]
                                jsondictxianxia[key] = v1[key]
                                jsondict1['成功']['线上对比成功'].update(jsondictxianshang)
                                jsondict1['成功']['线下对比成功'].update(jsondictxianxia)
                            elif key in v and key in v1 and v[key] not in v1[key]:
                                jsondictxianshang[key] = v[key]
                                jsondictxianxia[key] = v1[key]
                                jsondict['失败']['线上对比失败'].update(jsondictxianshang)
                                jsondict['失败']['线下对比失败'].update(jsondictxianxia)
                            elif key in v and key not in v1:
                                jsondictxianshang[key] = v[key]
                                jsondict['失败']['线上对比失败'].update(jsondictxianshang)
                            elif key not in v and key in v1:
                                jsondictxianxia[key] = v1[key]
                                jsondict['失败']['线下对比失败'].update(jsondictxianxia)
                            else:
                                dictnews = json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=2)
                                logbug.debug("日志记录:{}".format(dictnews))
                        dictnews1 = json.dumps(jsondict1, ensure_ascii=False, sort_keys=True, indent=2)
                        logger.info("日志记录---{}:{}".format(k, dictnews1))
                        dictnews = json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=2)
                        logbug.debug("日志记录---{}:{}".format(k, dictnews))
                        if jsondict['失败']['线上对比失败'] == {}:
                            duibi = '成功'
                        else:
                            duibi = '失败'
                        dictnew = dict(jsondict1,**jsondict)
                        dictnewww = json.dumps(dictnew, ensure_ascii=False, sort_keys=True, indent=2)
                        xubaojieguo = '无'
                        baojiajieguo = '无'
                        yongli = '无'
                        baofei = '无'
                        query_details = query_details_listna
                        views.details_data(k, gongshi, chengshi, xubaojieguo, baojiajieguo, yongli, dictnewww, duibi, baofei, query_details)

        return licenseno_open

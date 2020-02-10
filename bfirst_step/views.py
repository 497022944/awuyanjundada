from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import os,datetime,time
from bfirst_step import models
from bfirst_step.private_method.transmission_method import Run_case
from bfirst_step.private_method.renewal_method.maoyanceshi_method import Run_case
# Create your views here.

# 上传数据详情
def batch(request):
    global error, xianxiadir, xianshangdlr, query_batch_list,idds
    if request.method == 'POST':
        try:
            # 线上/线下id
            xianshangxianxia = request.POST.get('jkxianshangxianxia')
            # 操作人
            caozuoren = request.POST.get('jkcaozuoren', None)
            # 线上代理人id
            xianshangdlr = request.POST.get('jkxianshang', None)
            # 线下代理人id
            xianxiadir = request.POST.get('jkxianxia', None)
            # 报价城市id
            chengshi = request.POST.get('jkchengshi', None)
            # 保险公司id
            gongshi = request.POST.get('jkgongshi', None)
            # 场景id
            case = request.POST.get('jkcase', None)
            # 上传车牌
            fafafa = request.POST.get('fafafa')

            # 前端上传图片并且展示
            fafa = request.FILES.get('chepai')
            file_path = os.path.join('suplodfile', fafa.name)
            fa = open(file_path, mode='wb')
            for i in fafa.chunks():
                fa.write(i)
            fa.close()
            # 找车牌文件
            file_path = os.path.abspath(os.path.join(os.getcwd(), "./.")) + '\suplodfile\chepai.txt'
            # 打开文件
            file_open = open(file_path, 'r', encoding='utf-8-sig')
            # 加载文件
            licenseno_open = file_open.readlines()
            datetimenowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            zhixingzhuangtai = '已完成'
            storage_batch_listname(len(licenseno_open), zhixingzhuangtai, gongshi, case, xianshangdlr, xianxiadir, caozuoren, datetimenowTime)
            query_batch_list = query_batch_listname(request)
        except Exception:
            error = '参数不正确,请重新上传'
            return render(request, 'batch_list.html', {'error': error}, {'Query_doc': query_batch_list})
        else:
            # 查询操作人的id
            query_details_listna = query_details_listname(request, caozuoren)
            # 实例对比单程请求方法
            Run_casemethod = Run_case()
            # 获取续保，报价请求返回值 并入库
            testcase = Run_casemethod.test_01case(xianshangxianxia, xianshangdlr, xianxiadir, chengshi, gongshi, case, query_details_listna)
            print(query_batch_list)
            return render(request, 'batch_list.html', {'Query_doc': query_batch_list})
    elif request.method == 'GET':
        query_batch_list = query_batch_listname(request)
        idds = 1
        page_nubmer = request.GET.get('page', idds)
        cus_list = models.UserIifo.objects.order_by("-id")
        paginator = Paginator(cus_list, 10)
        pagunators = paginator.count
        page = paginator.page(int(page_nubmer))
        return render(request, 'batch_list.html', {'Query_doc': query_batch_list, 'page': page, 'paginator': paginator, 'pagunators': pagunators})

    else:
        query_batch_list = query_batch_listname(request)
        fengye = fenyessd(request,idds)
        return render(request, 'batch_list.html', {'Query_doc': query_batch_list})

#冒烟测试
def batchmanyan(request):
    try:
        # 操作人
        caozuoren = request.POST.get('jkcaozuoren', None)
        # 线上代理人id
        xianshangdlr = request.POST.get('jkxianshang', None)
        # 线下代理人id
        xianxiadir = request.POST.get('jkxianxia', None)
        # 报价城市id
        chengshi = request.POST.get('jkchengshi', None)
        # 保险公司id
        gongshi = request.POST.get('jkgongshi', None)
        # 上传车牌
        fafafa = request.POST.get('fafafa')

        # 前端上传图片并且展示
        fafa = request.FILES.get('chepai')
        file_path = os.path.join('suplodfile', fafa.name)
        fa = open(file_path, mode='wb')
        for i in fafa.chunks():
            fa.write(i)
        fa.close()
        # 找车牌文件
        file_path = os.path.abspath(os.path.join(os.getcwd(), "./.")) + '\suplodfile\maoyanchepai.txt'
        # 打开文件
        file_open = open(file_path, 'r', encoding='utf-8-sig')
        # 加载文件
        licenseno_open = file_open.readlines()
        Run_case.test_01maoyan(xianshangdlr, xianxiadir, chengshi, gongshi)
    except Exception:
        error = '参数不正确,请重新上传'
        return render(request, 'batch_list.html', {'error': error}, {'Query_doc': query_batch_list})

# 跳转数据详情列表
def details(request, id):
    query_details = query_strip_details_data(request, id)
    return render(request, 'details_list.html', {'query': query_details})

def login(request):
    return render(request, 'login.html')

# 批续列表存储数据库详情
def storage_batch_listname(licenseNumber, executionstate, Insurance, sceneid, sagent, xagent, founder, creationtime):
    # create 增加到表数据
    models.UserIifo.objects.create(
    # 车牌数量
    licenseNumber = licenseNumber,
    # 执行时间
    executionstate = executionstate,
    # 保险公司
    Insurance  = Insurance,
    # 场景id
    sceneid  = sceneid,
    # 线上代理人id
    sagent = sagent,
    # 线下代理人id
    xagent = xagent,
    # 创建人
    founder = founder,
    # 创建时间
    creationtime = creationtime,
    )

# details存储数据库详情
def details_data(licenseno, Insurance, cictcode, renewal, offer, sceneid, details, ontrast, insuredcontrast, strip):
    models.Data_details.objects.create(
    # 车牌号
    licenseno = licenseno,
    # 保险公司
    Insurance = Insurance,
    # 城市
    cictcode = cictcode,
    # 续保状态
    renewal = renewal,
    # 报价状态
    offer = offer,
    # 场景id
    sceneid = sceneid,
    # 详情--报价结果json
    details = details,
    # 对比结果
    ontrast = ontrast,
    # 保额保费对比
    insuredcontrast = insuredcontrast,
    # 批次id
    strip = strip,
    )

# details获取数据库详情
def query_details_data(request):
    query_datails = []
    datails = models.Data_details.objects.all()
    for row in datails:
       query_datails.append({'licenseno':row.licenseno, 'Insurance':row.Insurance, 'cictcode':row.cictcode, 'renewal':row.renewal, 'offer':row.offer, 'sceneid':row.sceneid, 'details':row.details, 'ontrast':row.ontrast, 'insuredcontrast':row.insuredcontrast, })
    return query_datails

# 批续列表获取数据库详情
def query_batch_listname(request):
    query_doc = []
    result = models.UserIifo.objects.all().order_by('-id')
    for row in result:
        query_doc.append({"id":row.id, "licenseNumber":row.licenseNumber, "executionstate":row.executionstate, "Insurance":row.Insurance, "sceneid":row.sceneid, "sagent":row.sagent, "xagent":row.xagent, "founder":row.founder, "creationtime":row.creationtime})
    return query_doc

# 批续列表点击删除，处理
def delete_details_listnames(request, id):
    # 调用单挑数据删除权限
    delete_details_listname(request, id)
    # 重新查询，并返回
    query_batch_list = query_batch_listname(request)
    return redirect('/batch/', {'Query_doc': query_batch_list})

# 批续单条查询 # 查询操作人
def query_details_listname(request, caozuoren):
    rows = '0'
    result = models.UserIifo.objects.last()
    rows = result.id
    return rows

# 批续查询ID 分页
def query_details_listnames(request):
    result = models.UserIifo.objects.all()
    rows = len(result)
    return rows

# 批续单条删除
def delete_details_listname(request, id):
    models.UserIifo.objects.filter(id=id).delete()

# details查询单条数据库详情
def query_strip_details_data(request, id):
    query_datail = []
    result = models.Data_details.objects.filter(strip=id)
    for row in result:
        query_datail.append(
            {'licenseno': row.licenseno, 'Insurance': row.Insurance, 'cictcode': row.cictcode, 'renewal': row.renewal,
             'offer': row.offer, 'sceneid': row.sceneid, 'details': row.details, 'ontrast': row.ontrast,
             'insuredcontrast': row.insuredcontrast})
    return query_datail

# 分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def fenyessd(request, id):
    #cus_list = models.UserIifo.objects.all()
    id = int(id)
    page_nubmer = request.GET.get('page', id)
    cus_list = models.UserIifo.objects.order_by("id")
    paginator = Paginator(cus_list, 10)
    pagunators = paginator.count
    page = paginator.page(int(page_nubmer))
    return render(request,'batch_list.html',locals())

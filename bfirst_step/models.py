from django.db import models

# Create your models here.

# 批续列表数据
class UserIifo(models.Model):
    # 批次id,自增，主键，不需要创建id

    # 车牌数量
    licenseNumber = models.CharField(max_length=64)
    # 执行状态
    executionstate = models.CharField(max_length=64)
    # 保险公司
    Insurance  = models.CharField(max_length=64)
    # 场景id
    sceneid  = models.CharField(max_length=64)
    # 线上代理人id
    sagent = models.CharField(max_length=64)
    # 线下代理人id
    xagent = models.CharField(max_length=64)
    # 创建人
    founder = models.CharField(max_length=64)
    # 创建时间
    creationtime = models.CharField(max_length=64)

# 批续详情列表
class Data_details(models.Model):
    # 提供批续查询id
    strip = models.CharField(max_length=64)
    # 车牌号
    licenseno = models.CharField(max_length=64)
    # 保险公司
    Insurance = models.CharField(max_length=64)
    # 城市
    cictcode = models.CharField(max_length=64)
    # 续保状态
    renewal = models.CharField(max_length=64)
    # 报价状态
    offer = models.CharField(max_length=64)
    # 场景id
    sceneid = models.CharField(max_length=64)
    # 详情--报价结果json
    details = models.CharField(max_length=64)
    # 对比结果
    ontrast = models.CharField(max_length=64)
    # 保额保费对比
    insuredcontrast = models.CharField(max_length=64)
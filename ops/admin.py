#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from ops import models


# # # #调整页面头部显示内容和页面标题

admin.site.site_header = "运维服务管理系统"
admin.site.site_title = "服务管理"


#注册到admin.site.register
# admin.site.register(models.Cis)
# admin.site.register(models.CiType,ci_tyepAdmin)
# admin.site.register(models.CiOrder,ci_orderAdmin)
# admin.site.register(models.CiProduct,ci_productAdmin)
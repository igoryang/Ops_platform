#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from time import timezone
import django.utils.timezone as timezone
import datetime

from pytz import utc

__author__ = 'igoryang'

from django.contrib import admin
from django.utils.text import capfirst
from django.utils.datastructures import SortedDict


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


registry = SortedDict()
registry.update(admin.site._registry)
admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)

from django.db import models
from django.utils.html import format_html  #设置字段颜色

# Create your models here.

# class Cis(models.Model):
#     class Meta:
#         db_table = 'cis'
#         verbose_name = verbose_name_plural = 'CIS'  # 表名称 别名 中文显示
#         ordering = ['cis_id']
#     #如果没有models.AutoField，默认会创建一个id的自增列
#     cis_id = models.AutoField(max_length=11, db_column='cis_id', primary_key=True)
#     type_id = models.IntegerField(max_length=11, db_column='type_id', blank=False)
#     status = models.CharField(max_length=8, db_column='status', null=True, blank=True)
#     created_time = models.DateTimeField(auto_now=True)
#     # update_time = models.DateTimeField(default=datetime.now().replace(tzinfo=utc))
#     heardbeat = models.DateTimeField(auto_now_add=True)
#       sex = models.BooleanField(max_length=1,choices=((0,'男'),(1,'女'),))
#     # color_code = models.CharField(max_length=6)
#     #
#     # def colored_name(self):  #字段颜色设置
#     #     return format_html(
#     #         '<span style="color:#{};">{} {}</span>',
#     #         self.color_code,
#     #         self.cis_id,
#     #         self.type_id,
#     #     )
#
#     def __str__(self):
#         return self.cis_id
#
#
# # 写法1  ci_type创建表名称， type_id创建字段名称  db_colunm=''创建列表名称 verbose_name=u""列表字段别名中文显示
# class CiType(models.Model):
#     class Meta:
#         db_table = 'ci_type'  # 创建表名称
#         verbose_name = '分类'  # 表名称 别名 中文显示
#         verbose_name_plural = '分类'  # 表名称 别名 中文显示
#         ordering = ['type_id']  # 排序字段
#
#     type_id = models.AutoField(max_length=11, db_column='type_id', primary_key=True,verbose_name=u'ID')  # db_column 创建列字段
#     type_name = models.CharField(max_length=50, db_column='type_name', verbose_name=u"类型")  # verbose_name字段中文显示
#     type_alias = models.CharField(max_length=50, db_column='type_alias', null=True, blank=True)
#     icon_url = models.CharField(max_length=255, db_column='icon_url', null=True, blank=True)  # blank 可以为空；填充null
#     order = models.SmallIntegerField(max_length=6, db_column='order', null=True, blank=True)
#     created_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#     uniq_id = models.IntegerField(max_length=11, db_column='uniq_id', null=True, blank=True)
#     status = models.CharField(max_length=8, db_column='status', null=True, blank=True)
#
#     def __str__(self):
#         return self.type_id
#     # def __unicode__(self):
#     #     return self.type_id
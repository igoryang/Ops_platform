# -*- encoding:utf-8 -*-

from django.shortcuts import render, HttpResponse
import json, chardet,os

# Create your views here.
from django.db import models
# from order.models import CiProduct   #导入 类 CiProduct
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #django 分页功能

def product(request):
    return render(request, 'ops/monitor.html')


# def product(request):
#     contacts_list = CiProduct.objects.all()  #列出ci_product表 所有数据
#     # print(p_list)
#     paginator = Paginator(contacts_list,25) #
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:
#         contacts = paginator.page(1)
#     except EmptyPage:
#         contacts = paginator.page(paginator.num_pages)
#
#     return render(request, 'order/product.html',{'product_list':contacts})
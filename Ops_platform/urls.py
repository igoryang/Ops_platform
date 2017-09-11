#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""Ops_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ops import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^dashboard/', include("order_cmdb.view.dashboard.urls")),
    url(r'^assets_management/', include("ops.view.assets_management.urls")),
    # url(r'^hosts_management/', include("ops.view.hosts_management.urls")),
    # url(r'^user_management/', include("ops.view.user_management.urls")),
    # url(r'^show_order/', include("order.view.show_order.urls")),
    # url(r'^time/$', include("admin.site.urls")),
    # url(r'^task', include("order_cmdb.view.task.urls")),
]

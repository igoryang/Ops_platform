# -*- coding: utf-8 -*-
from os import path
from django.apps import AppConfig
__author__ = 'igroyang'

VERBOSE_APP_NAME = u"运维服务管理系统"
def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]
class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'


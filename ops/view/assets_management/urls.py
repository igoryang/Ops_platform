#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.conf.urls import include, url
from ops.view.assets_management import assets_management

urlpatterns = [
    url(r'^$', assets_management.assets),
    url(r'^index$', assets_management.assets),
    # url(r'^lab$', product.lab),
    # url(r'^zone$', product.zone),
    # url(r'^cluster$', product.cluster),
    # url(r'^host$', product.host),
    # url(r'^vminstances$', product.vminstances),

]
#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.

# def index(request):
#     return render(request, 'index.html')
# from ops.models import


def login(request):
    return render(request, 'login.html')


def index(request):
    from ops import models
    return render(request, 'index.html')

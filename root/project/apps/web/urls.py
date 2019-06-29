# -*- coding:utf-8 -*-
__author__ = 'weixuefeng@lubangame.com'
__version__ = ''
__doc__ = ''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
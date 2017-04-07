#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:03:17 2017

@author: wanda

urls del blog 
"""

from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
    ]
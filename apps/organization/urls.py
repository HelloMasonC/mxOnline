#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from django.conf.urls import url, include

from .views import OrgView, AddUserAskView


__author__ = 'mc'


urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', ),
]

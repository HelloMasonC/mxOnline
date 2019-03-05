#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
__author__ = 'mc'
__date__ = '2019/02/01 11:33'

import xadmin
from xadmin import views

# from django.contrib.auth.models import Group
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台管理"
    site_footer = "监控分析室"
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time', 'add_time')
    search_fields = ('code', 'email', 'send_type', )
    list_filter = ('code', 'email', 'send_type', 'send_time', 'add_time')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'index', 'add_time', )
    search_fields = ('title', 'image', 'url', 'index', )
    list_filter = ('title', 'image', 'url', 'index', 'add_time',)


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
# xadmin.site.unregister(Group)
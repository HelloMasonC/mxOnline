#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

__author__ = 'mc'


# Create your views here.
class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 城市
        all_citys = CityDict.objects.all()
        categorys = {}
        for org in all_orgs:
            category_key = org.category
            category_value = org.get_category_display()
            if category_key not in categorys.keys():
                categorys[category_key] = category_value

        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'student':
                all_orgs = all_orgs.order_by('-student')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        org_num = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 对课程机构进行分页
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)
            
        return render(request, 'org_list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'categorys': categorys,
            'org_num': org_num,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        })
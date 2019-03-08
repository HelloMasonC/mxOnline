#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re
from django import forms

from operation.models import UserAsk

__author__ = 'mc'


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        TEL_REGEXP = '^[1]([3-9])[0-9]{9}$'
        p = re.compile(TEL_REGEXP)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code='mobile_invalid')
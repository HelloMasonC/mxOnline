# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-01-29 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courseresource_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]

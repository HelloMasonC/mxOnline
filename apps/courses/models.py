# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField('难度', max_length=10, choices=(('junior','初级'),('mid_level','中级'),('senior','高级')))
    learn_time = models.IntegerField('学习时长(分钟数)', default=0)
    students = models.IntegerField('学习人数', default=0)
    fav_nums = models.IntegerField('收藏人数', default=0)
    image = models.ImageField('logo', upload_to='course/%Y/%m')
    click_nums = models.IntegerField('点击数', default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField('章节名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
    
    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField('视频名', max_length=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField('名称', max_length=100)
    download = models.FileField('资源文件', upload_to='course/resource/%Y/%m')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = '课程资源'
    
    def __str__(self):
        return self.name
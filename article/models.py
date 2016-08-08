#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):

    title = models.CharField(max_length = 100 ) #文章标题
    category = models.CharField(max_length = 50, blank = True) #标签
    date_time = models.DateTimeField(auto_now_add = True) #日期
    content = models.TextField(blank = True, null = True) #正文

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_time']

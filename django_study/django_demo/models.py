from django.db import models

# Create your models here.

'''
创建UserInfo表

'''


class UserInfo(models.Model):
    # 创建第一列为username 必须指定一个最大长度
    username = models.CharField(max_length=32)
    # 创建一列为password
    password = models.CharField(max_length=32)
    # 一列为age
    age = models.IntegerField()

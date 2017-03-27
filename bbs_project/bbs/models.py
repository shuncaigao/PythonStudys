import datetime

from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
# 创建表结构

'''
    文章

'''


class Article(models.Model):
    # 作者
    author = models.ForeignKey('UserProfile')
    # 标题, 长度,
    title = models.CharField(max_length=255, unique=True)
    # 简介 长度,
    brief = models.TextField(max_length=512, default='none......')
    # 所属版块
    category = models.ForeignKey("Category")
    # 内容
    content = models.TextField(max_length=100000)
    # 发布时间
    pub_date = models.DateTimeField(blank=True, null=True)
    # 修改时间
    last_modify = models.DateTimeField(auto_now=True)
    # 优先级
    priority = models.IntegerField(u'优先级', default=1000)

    status_choices = (('draft', u'草稿'),
                      ('published', u'已发布'),
                      ('hidden', u'隐藏')
                      )
    status = models.CharField(max_length=250, choices=status_choices, default='published')

    head_img = models.ImageField(u'文章标题图片', upload_to='uploads')

    def __str__(self):
        return self.title

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError('Draft entries may not have a publication date.')
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


'''
    评论

'''


class Comment(models.Model):
    # 关联文章
    article = models.ForeignKey("Article", verbose_name=u'所属文章')
    # 父级评论
    parent_comment = models.ForeignKey('self', related_name='my_children', blank=True, null=True)

    #
    comment_choices = ((1, u'评论'),
                       (2, u'点赞'))
    # 文章评论还是点赞, 默认是点赞
    comment_type = models.IntegerField(choices=comment_choices, default=1)

    # 评论者
    user = models.ForeignKey('UserProfile')
    # 评论时间
    date = models.DateTimeField(auto_now_add=True)
    # 评论内容
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        if self.comment_type == 1 and len(self.comment) == 0:
            raise ValidationError(u'评论文章不能为空')

    def __str__(self):
        return '%s, P:%s, %s' % (self.article, self.parent_comment, self.comment)


'''
    版块

'''


class Category(models.Model):
    # 版块名字, 唯一
    name = models.CharField(max_length=32, unique=True)
    # 简介
    brief = models.CharField(null=True, blank=True, max_length=100)
    # 是否是顶部导航
    set_as_top_menu = models.BooleanField(default=False)

    # 展示位置
    position_index = models.SmallIntegerField()

    # 版主 默认可不选
    admins = models.ManyToManyField("UserProfile", blank=True)

    def __str__(self):
        return self.name


'''
    用户

'''


class UserProfile(models.Model):
    # 用户表 一对一
    user = models.OneToOneField(User)
    # 用户名字
    name = models.CharField(max_length=32)
    # 签名 可不写  可空
    signature = models.CharField(max_length=255, blank=True, null=True)
    # d头像 正方形, 可以为空, 可以不添加
    head_img = models.ImageField(height_field=150, width_field=150, blank=True, null=True)

    def __str__(self):
        return self.name

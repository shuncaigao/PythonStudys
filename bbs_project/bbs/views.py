from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from bbs import models

# Create your views here.
# 全局公用
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')


def index(request):
    return render(request, 'bbs/index.html', {'category_list': category_list})


def category(request, id):
    category_obj = models.Category.objects.get(id=id)

    # 显示全部
    if category_obj.position_index == 1:
        article_list = models.Article.objects.filter(status='published')
    else:
        # 通过id选择去显示文章
        article_list = models.Article.objects.filter(category_id=category_obj.id, status='published')
    return render(request, 'bbs/index.html', {'category_list': category_list,
                                              'category_obj': category_obj, 'article_list': article_list})

# def acc_login(request)

from django.shortcuts import render
from django.http import HttpResponse
from django_demo import models


# Create your views here.

def db(request):
    '''
        增
    '''

    # 第一种增加数据方式
    # models.UserInfo.objects.create(username='顺子', password='111111', age=25)
    # 第二种增加方式
    # dic = {'username': '顺子二号', 'password': '111111', 'age': 25}
    # models.UserInfo.objects.create(**dic)

    '''
        删
    '''
    # models.UserInfo.objects.filter(username='顺子').delete()
    '''
        改
    '''
    # models.UserInfo.objects.all().update(age=18)

    '''
        查
    '''
    # models.UserInfo.objects.filter(age=18)
    # models.UserInfo.objects.filter(age=18).first()

    if request.method == 'POST':
        print(request.POST['username'])

        # 插入数据
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'], )

    user_info = models.UserInfo.objects.all()
    return render(request, 'db.html', {'user_info': user_info})


def one(request, one):
    return HttpResponse(one)

def test(request, one):
    return HttpResponse(one)

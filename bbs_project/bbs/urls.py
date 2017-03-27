from django.conf.urls import url

from bbs import views

urlpatterns = [
    url(r'^$', views.index),
    # 共享一个界面
    url(r'^category/(\d+)/$', views.category),
]

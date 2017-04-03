"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django_demo import urls
from django_demo import views

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    # url(r'^db/', views.db),
    # url(r'^match/([0-9]+)/$', views.one),
    # url(r'^match/(p<year>[0-9]{4})/$', views.test)
    url(r'^demo/', include(urls))
}

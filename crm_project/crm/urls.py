from crm import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^customers/', views.customers),
]

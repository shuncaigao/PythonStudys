
from django.conf.urls import url
from django_demo import views

urlpatterns = {
    url(r'^db/', views.db),

}

from django import urls
from django.conf.urls import  url
from . import views

app_name="app1"


urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),

    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),


]
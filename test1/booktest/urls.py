from . import views
from django.conf.urls import url
app_name="booktest"
# 应用路由配置
urlpatterns=[

    url(r"^$",views.index,name="index")

]
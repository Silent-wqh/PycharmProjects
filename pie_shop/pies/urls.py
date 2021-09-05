"""定义pies的URL模式"""


from django.conf.urls import url

from . import views


urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的馅饼
    url(r'^pies$', views.pies, name='pies'),
    # 显示单一馅饼的全部信息
    url(r'^pies/(?P<pie_id>\d+)/$', views.pie, name='pie'),
]
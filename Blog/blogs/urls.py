from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 主题
    url(r'^blogs/$', views.title, name='title'),
    # 新建主题页面
    url(r'^new_blog/$', views.new_blog, name='new_blog'),
    # 编辑内容
    url(r'^blogs/(?P<blog_id>\d+)/$', views.edit_blog, name='edit_blog')
]
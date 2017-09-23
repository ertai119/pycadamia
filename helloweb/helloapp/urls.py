# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$', views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$', views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidates/(?P<name>[가-힣]+)/$', views.candidates),    
]
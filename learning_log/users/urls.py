#!/usr/bin/env python

"""为应用程序定义users定义URl模式"""


from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

# reviews/urls.py
app_name = 'reviews'
urlpatterns = [
	# 登陆界面
	url(r'^login/$', login, {'template_name': 'users/login.html'},
		name='login'),
	
	# 注销
	url(r'^logout/$', views.logout_view, name='logout'),
	
	# 注册页面
	url(r'^register/$', views.register, name='register')
	
	
]

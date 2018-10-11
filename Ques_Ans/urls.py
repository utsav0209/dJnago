from django.urls import path
from .views import  *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
        url(r'^ask/$', ask),
        url(r'^posted/$', posted),
        url(r'^answer/$', answer),
		url(r'^answer_posted/$',answer_posted),
]
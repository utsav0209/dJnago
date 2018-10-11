from django.urls import path
from .views import  *
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
        url(r'^login/$',auth_views.login , name ='login'),
        url(r'^auth/$', auth_view , name = 'loggedout'),
        #url(r'^logout/$', auth_views.login),
        url(r'^logout/$',logout),
        url(r'^loggedin/$', loggedin),
        url(r'^invalidlogin/$', invalidlogin),
        url(r'^register/$', register),
]
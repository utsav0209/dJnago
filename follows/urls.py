from django.conf.urls import url
from follows.views import *

urlpatterns = [
	url(r'^follow', follow),
]
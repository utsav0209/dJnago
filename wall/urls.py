from django.urls import path
from wall.views import  *
from django.conf.urls import url
from Ques_Ans.urls import *
from Ques_Ans.views import *
from wall.views import profile


urlpatterns = [
	url(r'^wall',wall),
	url(r'^Ques_Ans/answer',answer),
	url(r'^profile/$', profile),
	url(r'^search/$',search),
]

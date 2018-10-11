from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect  #for redirecting on failed login/logiut
from django.template.context_processors import csrf
from Ques_Ans.models import *
from login.models import *
from follows.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/login')
def wall(request):
    current_user = request.user
    name = current_user.username
    answers = Answer.objects.all()
    questions = Question.objects.all()
    return render(request , 'wall/showupdates.html',{'name': name, 'questions': questions, 'answers': answers,})


@login_required(login_url='/login/login')
def search(request):
    searched_user = request.GET.get('search')
    xuser = Client.objects.get(username=searched_user)
    questions = Question.objects.filter(user=xuser.User)
    answers = Answer.objects.filter(user=xuser.User)
    return render(request,'wall/search.html',{'searched_user':searched_user, 'questions': questions, 'answers': answers,})

	
@login_required(login_url='/login/login')
def profile(request):
	current_user = request.user
	name = current_user.username
	xuser = Client.objects.get(username=name)
	name = current_user.username
	QuerySet = Follows.objects.filter(person=current_user)
	return render(request, 'wall/profile.html', {'name':name,'people':QuerySet,'xuser':xuser})
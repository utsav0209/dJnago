from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/login')
def ask(request):
    return render(request, 'ask.html')


@login_required(login_url='/login/login')
def posted(request):
    user = request.user
    if request.POST.get('header') is not None:
        pheading = request.POST.get('header')
        pq_description = request.POST.get('description','')
        q = Question(user=user, heading=pheading, q_description=pq_description, reports=0, votes=0)
        q.save()
        return render(request, 'posted.html')


@login_required(login_url='/login/login')
def answer(request):
    q_id = request.GET.get("q_id")
    request.session['q_id']=int(q_id)
    return render(request, 'answer.html')


@login_required(login_url='/login/login')
def answer_posted(request):
	user = request.user
	q_id = request.session['q_id']
	del request.session['q_id']
	dans = request.POST.get('ans')
	a = Answer(user=user, question=q_id, votes=0, ans=dans)
	a.save()
	return  render(request, 'answer_posted.html')

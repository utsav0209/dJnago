from django.shortcuts import render
from follows.models import  *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/login')
def follow(request):
	current_user = request.user
	name = current_user.username
	to_follow = request.GET.get('user')
	p = Follows(person = current_user , following = to_follow)
	p.save()
	return render(request, 'followed.html',{'name': to_follow,})
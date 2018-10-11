from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect  #for redirecting on failed login/logiut
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from login.forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login,logout
from follows.models import Follows
from django.http import HttpResponse




def auth_view(request):
    uname = request.POST.get('username','')
    pword = request.POST.get('password','')
    user = auth.authenticate(username=uname , password= pword)  #check if username and password are correct, returns user if correct

    if user is not None:
        auth.login(request , user)
        return HttpResponseRedirect('/login/loggedin')  #redirect to logged in after logging in
    else:
        return HttpResponseRedirect('/login/invalidlogin')
		
		
@login_required(login_url='/login/login')
def loggedin(request):
    return render(request, 'login/loggedin.html')


@login_required(login_url='/login/login')
def invalidlogin(request):
    return render(request,'login/invalidlogin.html')

	
@login_required(login_url='/login/login')
def logout(request):
	auth.logout(request)
	return  render(request,'registration/logout.html')

	
def register(request):
    #if request.method == 'POST':
    #client_group = Group.objects.get(name = 'Client')
    user_form = UserCreationForm(request.POST)
    client_form = ClientForm(request.POST)
    if user_form.is_valid() and client_form.is_valid():
        user_instance = user_form.save(commit =False)
        #user_instance.set_password(user_form.cleaned_data.get('password1'))
        user_instance.is_staff = True
        user = user_instance.save()
        #user_instance.groups.add(client_group)
        client_instance = client_form.save(commit = False)
        client_instance.User = user_instance
        client_instance.save()
        return render(request , 'login/registered.html',{'client_instance' : client_instance })
    else:
        return render(request,'login/register.html', {'user_form' : user_form , 'client_form':client_form})




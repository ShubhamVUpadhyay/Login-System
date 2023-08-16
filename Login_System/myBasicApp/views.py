from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserinfoForm
from .models import Userinfo
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request,'myBasicApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'myBasicApp/index.html')

def user_login(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
               
            else:
                print("ACcount not Active")
        else:
            return HttpResponse("Invalid Login")
        
    else:
        return render(request,'myBasicApp/login.html')

def register(request):
    registered=False
    if request.method == 'POST':
        user_form=UserinfoForm(data=request.POST)
        if user_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form=UserinfoForm()

    return render(request,'myBasicApp/register.html',{'fn':user_form})
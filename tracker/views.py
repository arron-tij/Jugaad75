from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

from .models import classroom

# Create your views here.

def home(request):
    return render(request,'tracker/home.html')
   
def signupuser(request):

    if request.method =='GET':
        return render(request, 'tracker/signup.html',{ 'form': SignUpForm } )
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'] )
                user.save()

                class_code=request.POST['class_code']

                classroom.objects.create(student=user, class_code=class_code)

                print(class_code)

                login(request,user)
                return redirect('home')

            except IntegrityError:
               return render(request, 'tracker/signup.html',{ 'form': SignUpForm , 'error': 'Already Taken!..Please choose a new username' } ) 
        else:
            return render(request, 'tracker/signup.html',{ 'form': SignUpForm , 'error': 'Passwords not matched' } ) 
        

def loginuser(request):
    if request.method =='GET':
        return render(request, 'tracker/login.html',{ 'form': AuthenticationForm } )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'tracker/login.html',{ 'form': AuthenticationForm, 'error': 'Username and password does not match' } )
        else:
            login(request,user)
            return redirect('home')  

@login_required    
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

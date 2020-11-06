from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, addLectureForm
from .models import classroom,Lecture, lecture_copy

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# import time

# def getLocation():
#     options = Options()
#     options.add_argument("--use-fake-ui-for-media-stream")
#     timeout = 20
#     driver = webdriver.Chrome(executable_path = './chromedriver', chrome_options=options)
#     driver.get("https://mycurrentlocation.net/")
#     wait = WebDriverWait(driver, timeout)
#     time.sleep(3)
#     longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
#     longitude = [x.text for x in longitude]
#     longitude = str(longitude[0])
#     latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
#     latitude = [x.text for x in latitude]
#     latitude = str(latitude[0])
#     driver.quit()
#     return (latitude,longitude)
    
# Create your views here.

def home(request):

    l=lecture_copy.objects.all()
    return render(request,'tracker/home.html', {'lecture_copy': l})
   
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

                # print(class_code)

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

@login_required
def addLecture(request):

    table=Lecture.objects.filter(student=request.user).first()

    # Lecture.objects.all().delete()
    
    if Lecture.objects.filter(student=request.user):
        table=Lecture.objects.filter(student=request.user).first()
    else:
        table=Lecture.objects.create(student=request.user)

    if request.method == 'GET':
        form = addLectureForm(instance=table)
        return render(request, 'tracker/addLecture.html',{  'table': table, 'form': addLectureForm } )
    else:
        try:
            form = addLectureForm(request.POST,instance=table)
         
            # (lat,lon) = getLocation()  

            form.save()   
            
            # print('This is the location')
            # print(lat,lon)
            # print(request.user)

            l=Lecture.objects.filter(student=request.user).first()
            lecture_copy.objects.all().delete()
            
            if(l.monday_slot1_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.monday_slot1_name,lecture_count=0)
            if(l.monday_slot2_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.monday_slot2_name,lecture_count=0)
            if(l.monday_slot3_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.monday_slot3_name,lecture_count=0)               

            if(l.tuesday_slot1_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.tuesday_slot1_name,lecture_count=0)
            if(l.tuesday_slot2_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.tuesday_slot2_name,lecture_count=0)
            if(l.tuesday_slot3_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.tuesday_slot3_name,lecture_count=0)               

            if(l.wednesday_slot1_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.wednesday_slot1_name,lecture_count=0)
            if(l.wednesday_slot2_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.wednesday_slot2_name,lecture_count=0)
            if(l.wednesday_slot3_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.wednesday_slot3_name,lecture_count=0)   

            if(l.thrusday_slot1_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.thrusday_slot1_name,lecture_count=0)
            if(l.thrusday_slot2_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.thrusday_slot2_name,lecture_count=0)
            if(l.thrusday_slot3_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.thrusday_slot3_name,lecture_count=0)               

            if(l.friday_slot1_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.friday_slot1_name,lecture_count=0)
            if(l.friday_slot2_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.friday_slot2_name,lecture_count=0)
            if(l.friday_slot3_name!="None"):
                lecture_copy.objects.create(student=request.user,lecture_name=l.friday_slot3_name,lecture_count=0)               

              

            return redirect('home') 
        except ValueError:
            return render(request, 'tracker/addLecture.html',{ 'table': table, 'form': addLectureForm , 'error': 'Try again.. data is not valid' } )

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, addLectureForm
from .models import classroom,Lecture, lecture_copy, sdata
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import geopy.distance
from geopy.distance import geodesic
def getLocation():
    # Remove this next line
    # return (23.00,86.00)

    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome()
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude,longitude)

def getSlot():
    x = datetime.datetime.now()
    if x.hour>9 and x.hour<10:
        return 1
    elif x.hour>10 and x.hour<11:
        return 2
    elif x.hour>11 and x.hour<12:
        return 3
    return 4
    
def reqdLocation(clec):
    cslot = getSlot()
    x = datetime.datetime.today()
    if x.weekday() == 0:
        if cslot == 1:
            return (clec.monday_slot1_latitude,clec.monday_slot1_longitude,clec.monday_slot1_name)
        elif cslot == 2:
            return (clec.monday_slot2_latitude,clec.monday_slot2_longitude,clec.monday_slot2_name)
        elif cslot == 3:
            return (clec.monday_slot3_latitude,clec.monday_slot3_longitude,clec.monday_slot3_name)
        elif cslot == 4:
            return (0.0,0.0)
    elif x.weekday() == 1:
        if cslot == 1:
            return (clec.tuesday_slot1_latitude,clec.tuesday_slot1_longitude,clec.tuesday_slot1_name)
        elif cslot == 2:
            return (clec.tuesday_slot2_latitude,clec.tuesday_slot2_longitude,clec.tuesday_slot2_name)
        elif cslot == 3:
            return (clec.tuesday_slot3_latitude,clec.tuesday_slot3_longitude,clec.tuesday_slot3_name)
        elif cslot == 4:
            return (0.0,0.0)
    elif x.weekday() == 2:
        if cslot == 1:
            return (clec.wednesday_slot1_latitude,clec.wednesday_slot1_longitude,clec.wednesday_slot1_name)
        elif cslot == 2:
            return (clec.wednesday_slot2_latitude,clec.wednesday_slot2_longitude,clec.wednesday_slot2_name)
        elif cslot == 3:
            return (clec.wednesday_slot3_latitude,clec.wednesday_slot3_longitude,clec.wednesday_slot3_name)
        elif cslot == 4:
            return (0.0,0.0)
    elif x.weekday() == 3:
        if cslot == 1:
            return (clec.thrusday_slot1_latitude,clec.thrusday_slot1_longitude,clec.thrusday_slot1_name)
        elif cslot == 2:
            return (clec.thrusday_slot2_latitude,clec.thrusday_slot2_longitude,clec.thrusday_slot2_name)
        elif cslot == 3:
            return (clec.thrusday_slot3_latitude,clec.thrusday_slot3_longitude,clec.thrusday_slot3_name)
        elif cslot == 4:
            return (0.0,0.0)
    elif x.weekday() == 4:
        if cslot == 1:
            return (clec.friday_slot1_latitude,clec.friday_slot1_longitude,clec.friday_slot1_name)
        elif cslot == 2:
            return (clec.friday_slot2_latitude,clec.friday_slot2_longitude,clec.friday_slot2_name)
        elif cslot == 3:
            return (clec.friday_slot3_latitude,clec.friday_slot3_longitude,clec.friday_slot3_name)
        elif cslot == 4:
            return (0.0,0.0)
    else:
        return (0.0,2.0)
    

def home(request):
    curr_slot = getSlot()
    if request.user.is_authenticated and curr_slot != 4:
        clec = Lecture.objects.get(student=request.user)
        reqd_coord = reqdLocation(clec)
        if reqd_coord[0] == 0.00 and reqd_coord[1] == 0.00:
            return render(request,'tracker/home.html')
        curr_coord = getLocation()
        instance = sdata.objects.get(student=request.user)
        instance.slat = curr_coord[0]
        instance.slong = curr_coord[1]
        dist = geodesic(curr_coord, reqd_coord).km
        print(dist)
        dist = dist * 1000
        if dist < 50:
            if curr_slot == 1:
                instance.slot1 = 1
            elif curr_slot == 2:
                instance.slot2 = 1
            elif curr_slot == 3:
                instance.slot3 = 1
            instnc = lecture_copy.objects.get(student=request.user,lecture_name=reqd_coord[2])
            instnc.lecture_count = instnc.lecture_count + int(1)
            instnc.save()
        instance.save()
    return render(request,'tracker/home.html')
   
def signupuser(request):

    if request.method =='GET':
        return render(request, 'tracker/signup.html',{ 'form': SignUpForm } )
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'] )
                user.save()
                sdata.objects.create(student=user)
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

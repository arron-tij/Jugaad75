from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm

from .models import Lecture


class SignUpForm(UserCreationForm):
 
    class_code = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'class_code', 'password1', 'password2', )

class addLectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ( 'monday_slot1_name','monday_slot1_latitude' , 'monday_slot1_longitude',
        'monday_slot2_name','monday_slot2_latitude' , 'monday_slot2_longitude',
        'monday_slot3_name','monday_slot3_latitude' , 'monday_slot3_longitude',

        'tuesday_slot1_name','tuesday_slot1_latitude' , 'tuesday_slot1_longitude',
        'tuesday_slot2_name','tuesday_slot2_latitude' , 'tuesday_slot2_longitude',
        'tuesday_slot3_name','tuesday_slot3_latitude' , 'tuesday_slot3_longitude',

        'wednesday_slot1_name','wednesday_slot1_latitude' , 'wednesday_slot1_longitude',
        'wednesday_slot2_name','wednesday_slot2_latitude' , 'wednesday_slot2_longitude',
        'wednesday_slot3_name','wednesday_slot3_latitude' , 'wednesday_slot3_longitude',

        'thrusday_slot1_name','thrusday_slot1_latitude' , 'thrusday_slot1_longitude',
        'thrusday_slot2_name','thrusday_slot2_latitude' , 'thrusday_slot2_longitude',
        'thrusday_slot3_name','thrusday_slot3_latitude' , 'thrusday_slot3_longitude',

        'friday_slot1_name','friday_slot1_latitude' , 'friday_slot1_longitude',
        'friday_slot2_name','friday_slot2_latitude' , 'friday_slot2_longitude',
        'friday_slot3_name','friday_slot3_latitude' , 'friday_slot3_longitude'

        ) 

        
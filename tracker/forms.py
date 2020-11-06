from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
 
    class_code = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'class_code', 'password1', 'password2', )
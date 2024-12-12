## crm old project

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


from django.contrib.auth.models import auth

from .models import Employee #(forms)

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from captcha.fields import CaptchaField

#  register/ create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

# Create a login form

class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget = TextInput)
        password = forms.CharField(widget = PasswordInput)
    captcha = CaptchaField()
        # password = forms.PasswordInput(widget = PasswordInput)


# Creat Employee Records

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = ['first_name','last_name','email','phone','address','city','state','country']


# Update Record form

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','email','phone','address','city','state','country']
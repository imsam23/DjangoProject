from django import forms
from django.db import models
from models import *

""" We should create a ModelForm (docs), that has a field that uses the PasswordInput widget from the forms library. Here's what it would look like.
models.py

from django import models
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

forms.py (not views.py)

from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password': forms.PasswordInput(),
    }"""

#Each form field has a corresponding Widget class,
#  which in turn corresponds to an HTML form widget such as <input type="text">.
class Student_forms(forms.ModelForm):
    class Meta:
        model = Student
        widgets={'password':forms.PasswordInput(),}
        fields=('fisrt_name','last_name','user_id','password','state','Country')


class Login_form(forms.ModelForm):
    class Meta:
        model=Student
        widgets={'password':forms.PasswordInput(),}
        fields=('user_id','password')




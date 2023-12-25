from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmpFormClass (forms.Form):

    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    joiningdate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

class UserRegister(UserCreationForm):
    
    class Meta:
        model=User
        
        fields=['username','first_name','last_name','email']


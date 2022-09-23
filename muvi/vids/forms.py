from dataclasses import field
from django.core import validators
from django import forms
from django.contrib.auth.models import User

class userRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        
class loginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']        
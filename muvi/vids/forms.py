from dataclasses import field
from django.core import validators
from django import forms
from django.contrib.auth.models import User
from .models import reels

class userRegister(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        
class loginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']  
        
class videoForm(forms.ModelForm):
    class Meta:
        model=reels
        fields=['caption','reel','desc'] 
        widgets = {
          'desc': forms.Textarea(attrs={'rows':4, 'cols':100}),
        }              
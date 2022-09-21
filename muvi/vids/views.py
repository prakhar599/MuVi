from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect
from .models import reels,User
from .forms import userRegister
from  django.http import HttpResponse


class mypage(View):
    def get(self,request):
        videos = reels.objects.all()
        return render(request,'vids/main.html',{'videos':videos})
    
    def post(self,request):
        return
    
class register(View):
    def get(self,request):
        fm = userRegister()
        return render(request,'vids/register.html',{'form':fm})
    
    def post(self,request):
        fm = userRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email=em, password=pw)
            reg.save()
            return redirect('/vids')
    
   
    

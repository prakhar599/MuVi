from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect
from .models import reels
from .forms import userRegister,loginForm
from  django.http import HttpResponse
import numpy as np
import cv2 as cv
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages 
from django.contrib.auth.models import User




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
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User.objects.create_user(username = nm, email=em, password=pw)
            reg.save()
            return redirect('/vids')
        
class upload(View):
    def get(self,request):
        cap = cv.VideoCapture(0)
        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        out = cv.VideoWriter('D:/video.mp4', fourcc, 20.0, (640,  480))
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break
        # Release everything if job is finished
        cap.release()
        out.release()
        cv.destroyAllWindows()
        
        caption = 'new cap'
        desc = 'new desc'
        reels.reel.path = 'shorts/output1.mp4'
        print(caption)
        print(desc)
        print(reels.reel.path)
        new = reels(caption=caption,reel=reels.reel.path,desc=desc)
        new.save()
        return HttpResponse('done')

    
    def post(self,request):
            return redirect('/vids')     
        
class login(View):
    def post(self,request):     
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")     
        user = authenticate(request , username = name, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request,'logging in successful !')
            return redirect('/vids') 
        else:
            messages.warning(request,' Incorrect Credentials or account does not exist')
            return render(request,'vids/failure.html')
                       
    def get(self,request):
        form = loginForm()     
        return render(request,'vids/login.html',context = {'form':form})
    
def logout(request):
    auth_logout(request)
    return redirect('/vids')               
    
   
    

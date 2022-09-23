from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect
from .models import reels,User
from .forms import userRegister
from  django.http import HttpResponse
import numpy as np
import cv2 as cv


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
    
   
    

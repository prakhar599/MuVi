from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import mypage,register,upload

urlpatterns = [
    path('', mypage.as_view(),name='mypage'),
    path('signup',register.as_view(),name='signup'),
    path('upload',upload.as_view(),name='upload')
 
    

]



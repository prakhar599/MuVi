from django.db import models

class reels(models.Model):
    caption = models.CharField(max_length=100)
    reel = models.FileField(upload_to='shorts/')
    desc = models.CharField(max_length=300 , null=True)
    
    def __str__(self):
        return self.caption
    
class User(models.Model):
    name = models.CharField(max_length=50)    
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

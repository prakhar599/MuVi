from django.db import models

class reels(models.Model):
    caption = models.CharField(max_length=100)
    reel = models.FileField(upload_to='shorts/')
    desc = models.TextField(max_length=300 , null=True)
    
    def __str__(self):
        return self.caption
    

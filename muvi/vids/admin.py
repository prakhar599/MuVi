from django.contrib import admin
from .models import reels,User
admin.site.register(reels)
admin.site.register(User)

# @admin.register(reels)
# class reelsAdmin(admin.ModelAdmin):
#     list_display=['id','caption','reel']

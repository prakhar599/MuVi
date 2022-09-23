from django.contrib import admin
from .models import reels
admin.site.register(reels)


# @admin.register(reels)
# class reelsAdmin(admin.ModelAdmin):
#     list_display=['id','caption','reel']

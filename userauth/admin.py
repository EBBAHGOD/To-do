from django.contrib import admin
from .models import User
# Register your models here.

class user_rep(admin.ModelAdmin):
    list_display=['email','date_joined','username']





admin.site.register(User,user_rep)
from django.contrib import admin
from base.models import task
# Register your models here.





class taskview(admin.ModelAdmin):
    list_display=['title','user','created']


admin.site.register(task,taskview)














# class useradmin(admin.ModelAdmin):
#     list_display=['email','date_joined'] #list_diplay contains the list of fields to display for a model
#     list_per_page=10 #this helps to control the number of list item to display per page

# admin.site.register(user_details,useradmin) #in registering the model you associate it with the admin class that should control how the model is displayed
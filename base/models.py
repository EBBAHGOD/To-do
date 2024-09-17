from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # to help in linking the custom user model from settings to the task model



class task(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)  #automatically writes the date the instance of the model was created
    

    def __str__(self):
        return self.title


    class Meta:
        ordering=['complete']
















    # Create your models here.
# class user_details(AbstractUser):

#     email=models.EmailField(unique=True)
#     username=models.CharField(max_length=20)
#     dp=models.ImageField
#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS=['username']
    

#     def __str__(self):
#         return self.username
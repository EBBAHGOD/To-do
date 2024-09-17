

from django.shortcuts import render
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def loginview(request):
    if request.method =="POST":
        
        email=request.POST['email'] #collect email
        password=request.POST['password'] #coleect password
        validated_user=authenticate(email=email,password=password) #validates if a user matches with the password and email and returns a user object
        
        if validated_user is not None: # if a user object was returned 
            login(request,validated_user) #login the user using the user object
            return redirect('tasks') # return the user to the home or tasks page
        else: # if a user is not found
            email_check=User.objects.filter(email=email) # check to seee if the email is in the database
            if email_check: # if the email is in the database 
                 messages.error(request,"incorrect email or password") #Prompt the use of incorect email or password
                 return redirect('login')
            else:
                messages.error(request,"Account not found") # if the email is not found telll the user the account was not found
                return redirect('login') 


    else:
    
        return render(request,'auth/login.html')
    
def signupview(request):
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
        
            
            if len(password1)<=3:
                messages.error(request,"password lenth too short")
                return redirect('signup')
            
            email_taken=User.objects.filter(email=email) #checking if the email is already in the database
            if email_taken:
                messages.error(request,"Email taken")
                return redirect('signup')

            username_taken=User.objects.filter(username=username)
            if username_taken:
                messages.error(request,"username taken")
                return redirect('signup')
                

            new_user=User.objects.create_user(username=username,password=password1,email=email)
            
            new_user.save()
            authenticated_user=authenticate(email=email,password=password1)
            login(request,authenticated_user)
            return redirect('tasks')
        else:
            messages.error(request,'oops passwords do not match')
            return redirect('signup')

    else:
        return render(request,'auth/signup.html')
    
def logoutview(request):
    logout(request)
    return redirect('tasks')

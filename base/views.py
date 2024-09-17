from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models  import task
from userauth.models import User

# Create your views here.
def task_list(request):
    if request.method=='POST':
        taskname=request.POST['ent_task']
        new_task=task(user=request.user,title=taskname)
        new_task.save()
        return redirect('tasks')

        

    else:
        context = {'todos': []}
        if request.user.is_authenticated:
            all_todos=task.objects.filter(user=request.user)
            context={'todos':all_todos}
        return render(request,'base/base.html',context)
    
def deleteview(request,title_name):
    to_del=task.objects.filter(user=request.user,title=title_name)
    to_del.delete()
    return redirect('tasks')

def finished(request,name):
    to_update=task.objects.filter(user=request.user,title=name)
    for item in to_update:
        item.complete=True
        item.save()
    return redirect('tasks')

def restart_view(request,name):
    to_restart=task.objects.filter(user=request.user,title=name)
    for item in to_restart:
        item.complete=False
        item.save()
        return redirect('tasks')

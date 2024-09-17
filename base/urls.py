from django.urls import path
from . import views
urlpatterns = [
    path('',views.task_list,name="tasks"),
    path('delete/<str:title_name>',views.deleteview,name='delete'),
    path('completed/<str:name>',views.finished,name='completed'),
    path('restart/<str:name>',views.restart_view,name='restart')
]
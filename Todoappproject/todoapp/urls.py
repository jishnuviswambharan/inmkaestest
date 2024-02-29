from . import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [

    # function type views URL
    path('',views.home, name='home'),
    path('details', views.details, name='details'),
    path('delete/ <int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    #class type views URL

    path('cbvlist/', views.TaskLiseView.as_view(), name='cbvlist'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name = 'cbvdelete')

]
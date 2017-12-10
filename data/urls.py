from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/todo_detail/', views.todo_detail, name='todo_detail'),
    path('todo_new/', views.todo_new, name='todo_new'),
    path('<int:pk>/todo_edit/', views.todo_edit, name='todo_edit'),
]
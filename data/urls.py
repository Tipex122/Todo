from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/todo_detail/', views.todo_detail, name='todo_detail'),
]
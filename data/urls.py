from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/todo_detail/', views.todo_detail, name='todo_detail'),
    path('todo_new/', views.todo_new, name='todo_new'),
    path('<int:pk>/todo_edit/', views.todo_edit, name='todo_edit'),
    path('<int:pk>/todo_checked/', views.todo_checked, name='todo_checked'),
    path('<int:pk>/todo_list_by_category/', views.todo_list_by_category, name='todo_list_by_category'),

    path('categories_list/', views.categories_list, name='categories_list'),
    path('category_new/', views.category_new, name='category_new'),
    path('<int:pk>/category_edit/', views.category_edit, name='category_edit'),
]

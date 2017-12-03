from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request,'app/todo_list.html', context)



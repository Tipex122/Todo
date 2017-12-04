from django.shortcuts import render, get_object_or_404

# Create your views here.

# from django.http import HttpResponse
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request,'data/todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'data/todo_detail.html', {'todo': todo})


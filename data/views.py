from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

# from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request,'data/todo_list.html', context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'data/todo_detail.html', {'todo': todo})


def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()

    return render(request, 'data/todo_edit.html', {'form': form})
    # return render(request,'data/todo_edit.html',{'form': form})


def todo_edit(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = TodoForm(instance=post)
    return render(request, 'data/todo_edit.html', {'form': form})


def todo_checked(request, pk):
    post = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=post)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=post.pk)
    else:
        form = TodoForm(instance=post)
    return render(request, 'data/todo_edit.html', {'form': form})


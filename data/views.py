from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

# from django.http import HttpResponse
from .models import Todo, Category
from .forms import TodoForm, CategoryForm


def categories_list(request):
    categories = Category.objects.all()
    # print(categories)
    context = {'categories': categories, }
    return render(request, 'data/categories_list.html', context)


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()

    return render(request, 'data/category_edit.html', {'form': form})
    # return render(request,'data/todo_edit.html',{'form': form})


def category_edit(request, pk):
    post = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=post)
        if form.is_valid():
            category = form.save(commit=False)
            # category.user = request.user
            # category.created_date = timezone.now()
            category.save()
            return redirect('categories_list')  # , pk=post.pk)
    else:
        form = CategoryForm(instance=post)
    return render(request, 'data/category_edit.html', {'form': form})


def index(request):
    todos = Todo.objects.all()
    nbr = todos.count()
    context = {'todos': todos, 'nbr': nbr, }
    return render(request,'data/todo_list.html', context)


def todo_list_by_category(request, pk):
    todos = Todo.objects.filter(category__id=pk).filter(user=request.user)
    nbr = todos.count()
    context = {'todos': todos, 'nbr': nbr, }
    return render(request, 'data/todo_list.html', context)


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
    # post = get_object_or_404(Todo, pk=pk)
    # print(post.is_finished)
    # post.is_finished = True
    todo = Todo.objects.get(pk=pk)
    if todo.is_finished:
        todo.is_finished = False
    else:
        todo.is_finished = True

    todo.save()
    # print(todo)
    # print(todo.is_finished)
    return redirect('home')

'''
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

'''
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()

    return render(request, 'todoapp/index.html', {'todos': todos})

@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    if len(title) > 0:
        todo = Todo(title=title)
        todo.save()

    return redirect("home")

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo:
        todo.is_complete = not todo.is_complete
        todo.save()

    return redirect("home")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo:
        todo.delete()

    return redirect("home")

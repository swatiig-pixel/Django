from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def index(request):
  if request.method == "POST":
    title = request.POST.get("task")
    Task.objects.create(title=title)

  tasks = Task.objects.all()
  return render(request, "index.html",{"tasks":tasks})

def delete_task(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect('/')

def complete_task(request, id):
  task = Task.objects.get(id=id)
  task.completed = True
  task.save()
  return redirect('/')
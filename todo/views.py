from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from.models import Task
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')

def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsUnDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method =='POST':
        task_name = request.POST['task_name']
        task.task = task_name
        task.save()
        return redirect('home')
    else:
        context = {
            'task':task,
        }
    return render(request, 'edit_task.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
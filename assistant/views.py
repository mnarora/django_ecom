from django.shortcuts import render
from django.http import HttpResponse
from .models import task
# Create your views here.
def assistant(request):
    tasks = task.objects.all()
    params ={'tasklist' : tasks}
    return render(request, 'assistant/index.html', params)

def todolist(request):
    return render(request, 'assistant/todolist.html', {})


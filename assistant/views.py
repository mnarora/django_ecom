from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import task
from .models import todolist
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def assistant(request):
    tasks = task.objects.all()
    params ={'tasklist' : tasks}
    return render(request, 'assistant/index.html', params)

def todoList(request, idz, typer):
    print(typer)
    if request.POST and typer == 'add':
        mtitle = request.POST.get('title', 'default')
        mdescription = request.POST.get('description', 'default')
        tolist = todolist(title = mtitle, Description = mdescription)
        tolist.save()
    if typer == 'del':
        a = todolist.objects.all()
        a[idz - 1].delete()
    if typer == 'clear':
        a = todolist.objects.all()
        a.delete()
    tasks = todolist.objects.all()
    params ={'tasklist' : tasks}
    return render(request, 'assistant/todolist.html', params)

def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginuname']
        passw = request.POST['loginpass']

        user = authenticate(username=loginusername, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect('assistant')
        else:
            return HttpResponse('Invalid Credentials')
    return HttpResponse('404 Not Found')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['uname']
        lname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username, email, pass1)
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('assistant')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('assistant')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been successfully created")
        return redirect('assistant')
    else:
        return HttpResponse('404-Not Found')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('assistant')

def Expense(request):
    return render(request, 'assistant/expense.html')
from django.shortcuts import render, redirect
from matplotlib import pyplot as plt 
from django.http import HttpResponse
from .models import task
from .models import todolist
from .models import ExpenseInfo
from .models import Goals
from .models import Bday
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import warnings
import datetime
import smtplib
from email.message import EmailMessage
import wikipedia

# Create your views here.
def assistant(request):
    tasks = task.objects.all()
    params ={'tasklist' : tasks}
    return render(request, 'assistant/index.html', params)

def todoList(request, idz, typer):
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

def Expense(request, idz, typer):
    if request.POST and typer == 'add':
        mtitle = request.POST.get('title', 'default')
        mdescription = request.POST.get('amount', 'default')
        expdate = request.POST.get('amountdate', 'default')
        d = datetime.date(int(expdate[:4]), int(expdate[5:7]), int(expdate[8:10]))
        expcat = request.POST.get('expcateg', 'default')
        tolist = ExpenseInfo(expense_item = mtitle, expense_cost = mdescription, date_added = d, expense_cat = expcat)
        tolist.save()
    if typer == 'del':
        a = ExpenseInfo.objects.all()
        a[idz - 1].delete()
    if typer == 'clear':
        a = ExpenseInfo.objects.all()
        a.delete()
    emp ={}
    tasks = ExpenseInfo.objects.all()
    for i in tasks:
        if i.expense_cat in emp:
            emp[i.expense_cat] += i.expense_cost
        else:
            emp[i.expense_cat] = i.expense_cost
    warnings.simplefilter('ignore')
    fig = plt.figure(figsize =(6, 4)) 
    plt.pie(list(emp.values()), labels = list(emp.keys())) 
    plt.savefig('media/assistant/images/expense.jpg') 
    params ={'tasklist' : tasks, 'pie' : len(emp)}
    return render(request, 'assistant/expense.html', params)

def goals(request, idz, typer):
    if request.POST and typer == 'add':
        goal_name  = request.POST.get('title', 'default')
        goal_prog = request.POST.get('goalprog', 'default')
        goal = Goals(Goals_desc = goal_name, Goals_prog = goal_prog)
        goal.save()
    if request.POST and typer == 'edit':
        a = Goals.objects.all()
        b = Goals.objects.get(Goals_desc = a[idz - 1].Goals_desc)
        b.Goals_prog = request.POST.get('goalProg')
        b.save()
    if typer == 'del' and len(Goals.objects.all()) != 0:
        a = Goals.objects.all()
        a[idz - 1].delete()
    if typer == 'clear':
        a = Goals.objects.all()
        a.delete()
    tasks = Goals.objects.all()
    
    sum = 0
    if len(tasks) != 0:
        for i in tasks:
            sum += i.Goals_prog
        sum /= len(tasks)
    params ={'tasklist' : tasks, 'perc':sum}
    return render(request, 'assistant/goals.html', params)

def birthday(request, idz, typer):
    if request.POST and typer == 'add':
        fr_name = request.POST.get('frename', 'default')
        fr_date = request.POST.get('birthdate')
        d = datetime.date(int(fr_date[:4]), int(fr_date[5:7]), int(fr_date[8:10]))
        temp = Bday(bday_name = fr_name, bday_date = d)
        temp.save()
    tasks = Bday.objects.all()
    for i in tasks:
        if i.bday_date.month == datetime.date.today().month and i.bday_date.day == datetime.date.today().day:
            messages.success(request, "Its " + i.bday_name+"'s birthday today.")
    params = {'tasklist':tasks}
    return render(request, 'assistant/bday.html', params)
    
def miniGoogle(request, task):
    if request.POST and task == 'email':
        senemail = request.POST.get('sendersemail')
        print(senemail, request.POST.get('senderspass'), request.POST.get('emailmessage', ''), request.POST.get('subject', ''), request.POST.get('recipientsemail'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(senemail, request.POST.get('senderspass'))
        msg = EmailMessage()
        msg.set_content(request.POST.get('emailmessage', ''))
        msg['Subject'] = request.POST.get('subject', '')
        msg['From'] = senemail
        msg['To'] = request.POST.get('recipientsemail')
        s.send_message(msg)
        s.quit()
        """s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 
        s.login(senemail, request.POST.get("senderpass", ""))
        msg = EmailMessage()
        msg.set_content(request.POST.get("emailmessage", ""))
        msg['Subject'] = request.POST.get("subject", "")
        msg['From'] = "wethestockedpantry@gmail.com"
        msg['To'] = "mnarora2000@gmail.com"
        s.send_message(msg)
        s.quit()"""
        messages.success(request, "Email sent successfully")
    if request.POST and task == 'search':
        query = request.POST.get('searchtext')
        query = query + " wikipedia"
        results = wikipedia.summary(query, sentences=3)
        print(query)
        print(results)
        params = {'tasklist':results}
        return render(request, 'assistant/minigoogle.html', params)
    return render(request, 'assistant/minigoogle.html')

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



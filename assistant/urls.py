from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.assistant, name = 'assistant'),
    path('admin/', admin.site.urls),
    path('todolist/<int:idz>/<str:typer>', views.todoList, name = 'tolist'),
    path('login', views.Login, name = 'LogIn'),
    path('signup', views.Signup, name = 'SignUp'),
    path('logout', views.Logout, name = 'LogOut'),
    path('expense/<int:idz>/<str:typer>', views.Expense, name = 'Expense'),
    path('goals/<int:idz>/<str:typer>', views.goals, name = 'goals'),
    path('birthday/<int:idz>/<str:typer>', views.birthday, name = 'biday'),
    path('minigoogle/<str:task>', views.miniGoogle, name = 'minigoogle'),
    path('password/<int:idz>/<str:typer>', views.passw, name='passw'),
]
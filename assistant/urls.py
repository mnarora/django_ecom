from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.assistant, name = 'assistant'),
    path('admin/', admin.site.urls),
    path('todolist/', views.todolist, name = 'todolist'),
]
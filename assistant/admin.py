from django.contrib import admin
from .models import task
from .models import todolist

admin.site.register(task)
admin.site.register(todolist)
# Register your models here.

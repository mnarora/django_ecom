from django.contrib import admin
from .models import task
from .models import todolist
from .models import ExpenseInfo

admin.site.register(task)
admin.site.register(todolist)
admin.site.register(ExpenseInfo)
# Register your models here.

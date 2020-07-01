from django.contrib import admin
from .models import task
from .models import todolist
from .models import ExpenseInfo
from .models import Goals

admin.site.register(task)
admin.site.register(todolist)
admin.site.register(ExpenseInfo)
admin.site.register(Goals)
# Register your models here.

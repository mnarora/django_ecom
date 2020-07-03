from django.contrib import admin
from .models import task
from .models import todolist
from .models import ExpenseInfo
from .models import Goals
from .models import Passstore
from .models import Bday

admin.site.register(task)
admin.site.register(todolist)
admin.site.register(ExpenseInfo)
admin.site.register(Goals)
admin.site.register(Passstore)
admin.site.register(Bday)
# Register your models here.
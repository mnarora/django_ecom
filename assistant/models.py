from django.db import models

# Create your models here.
class task(models.Model):
    task_name = models.CharField(max_length = 40)
    task_desc = models.CharField(max_length = 200)
    task_ima = models.ImageField(upload_to = 'assistant/images/')
    task_url = models.CharField(max_length = 40, default = '#')
    def __str__(self):
        return self.task_name

class todolist(models.Model):
    title = models.CharField(max_length = 80)
    Description = models.CharField(max_length = 300)
    def __str__(self):
        return self.title

class ExpenseInfo(models.Model):
    expense_item = models.CharField(max_length=80)
    expense_cost = models.FloatField()
    date_added = models.DateField()
    expense_cat = models.CharField(max_length=10, default = 'Others')
    def __str__(self):
        return self.expense_item

class Goals(models.Model):
    Goals_desc = models.CharField(max_length = 40)
    Goals_prog = models.IntegerField(default = 0)
    def __str__(self):
        return self.Goals_desc

class Passstore(models.Model):
    account = models.CharField(max_length = 20)
    account_pass = models.CharField(max_length = 20)
    def __str__(self):
        return self.account

class Bday(models.Model):
    bday_name = models.CharField(max_length = 20)
    bday_date = models.DateField()
    def __str__(self):
        return self.bday_name
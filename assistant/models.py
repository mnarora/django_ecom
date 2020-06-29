from django.db import models

# Create your models here.
class task(models.Model):
    task_name = models.CharField(max_length = 40)
    task_desc = models.CharField(max_length = 200)
    task_ima = models.ImageField(upload_to = 'assistant/images/')
    task_url = models.CharField(max_length = 20, default = '#')
    def __str__(self):
        return self.task_name

class todolist(models.Model):
    title = models.CharField(max_length = 80)
    Description = models.CharField(max_length = 300)
    def __str__(self):
        return self.title
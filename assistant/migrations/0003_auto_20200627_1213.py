# Generated by Django 2.2.10 on 2020-06-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0002_auto_20200627_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_ima',
            field=models.ImageField(default='../default.png', upload_to='assistant/images'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-07-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0016_bday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passstore',
            name='account_pass',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_url',
            field=models.CharField(default='#', max_length=40),
        ),
    ]

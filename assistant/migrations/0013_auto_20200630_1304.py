# Generated by Django 2.2.10 on 2020-06-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0012_auto_20200630_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinfo',
            name='date_added',
            field=models.DateField(),
        ),
    ]

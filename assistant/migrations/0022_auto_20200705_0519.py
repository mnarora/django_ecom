# Generated by Django 2.2.10 on 2020-07-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0021_passstore_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bday',
            name='bday_name',
            field=models.CharField(max_length=200),
        ),
    ]
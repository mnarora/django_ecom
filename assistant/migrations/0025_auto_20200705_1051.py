# Generated by Django 2.2.10 on 2020-07-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0024_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passstore',
            name='account_pass',
            field=models.CharField(max_length=20),
        ),
    ]
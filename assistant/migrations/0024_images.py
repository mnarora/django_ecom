# Generated by Django 2.2.10 on 2020-07-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0023_auto_20200705_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_image', models.ImageField(upload_to='assistant/images')),
            ],
        ),
    ]

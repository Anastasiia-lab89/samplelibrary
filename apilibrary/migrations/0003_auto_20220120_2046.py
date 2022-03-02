# Generated by Django 3.1.3 on 2022-01-20 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apilibrary', '0002_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='year',
        ),
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
        migrations.AddField(
            model_name='author',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата выпуска книги'),
        ),
    ]

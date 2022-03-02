# Generated by Django 3.1.3 on 2022-01-20 17:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО автора')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год рождения')),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название книги')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год выпуска книги')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apilibrary.author', verbose_name='Автор книги')),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Наименование жанра')),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название библиотеки')),
                ('address', models.CharField(default='', max_length=150, verbose_name='Адрес')),
                ('start_time', models.TimeField(verbose_name='Начало работы')),
                ('end_time', models.TimeField(verbose_name='Окончание работы')),
            ],
            options={
                'db_table': 'libraries',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_fio', models.CharField(max_length=150, verbose_name='ФИО автора комментария')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Дата комментария')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apilibrary.book', verbose_name='Книга')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apilibrary.genre', verbose_name='Жанр книги'),
        ),
    ]

import datetime

from django.contrib.auth.models import User
from django.db import models
# from rest_framework.authtoken.admin import User


class Genre(models.Model):
    name = models.CharField('Наименование жанра', max_length=100, default='')

    class Meta:
        db_table = 'genres'


class Library(models.Model):
    name = models.CharField('Название библиотеки', max_length=150)
    address = models.CharField('Адрес', max_length=150, default='')
    start_time = models.TimeField(verbose_name='Начало работы')
    end_time = models.TimeField(verbose_name='Окончание работы')

    class Meta:
        db_table = 'libraries'


class Book(models.Model):
    name = models.CharField('Название книги', max_length=150)
    date = models.DateField('Дата выпуска книги', default=datetime.datetime.now)
    author = models.ForeignKey('Author', verbose_name='Автор книги', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', verbose_name='Жанр книги', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'


class Author(models.Model):
    fio = models.CharField('ФИО автора', max_length=150)
    date = models.DateField('Дата рождения', default=datetime.datetime.now)

    class Meta:
        db_table = 'authors'


class Comment(models.Model):
    author_fio = models.CharField('ФИО автора комментария', max_length=150)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)
    date = models.DateField('Дата комментария', default=datetime.datetime.now)
    text = models.CharField('Текст комментария', max_length=100, default='')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

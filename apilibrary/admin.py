from django.contrib import admin

from apilibrary.models import Genre, Library, Book, Author, Comment

admin.site.register(Genre)
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comment)

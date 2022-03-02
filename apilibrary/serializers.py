from rest_framework import serializers
from apilibrary.models import Book, Genre, Comment, Author


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

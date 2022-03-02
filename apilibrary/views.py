from rest_framework import authentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apilibrary.models import Book, Genre, Comment, Author
from apilibrary.permissions import HasEditPermission
from apilibrary.serializers import BooksSerializer, GenresSerializer, Commentserializer, AuthorsSerializer


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.prefetch_related('comment_set')
    http_method_names = ['get', 'put', 'patch', 'delete']
    permission_classes = [IsAuthenticated]


class GenresViewSet(ModelViewSet):
    serializer_class = GenresSerializer
    queryset = Genre.objects.all()
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]


class BookCommentsViewSet(ModelViewSet):
    serializer_class = Commentserializer
    queryset = Comment.objects.all()
    http_method_names = ['get', 'post']
    permission_classes = [
        IsAuthenticated,
        HasEditPermission,
    ]

    def get_queryset(self, ):
        return Comment.objects.filter(book_id=self.kwargs['book__pk'])


class AuthorsViewSet(ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Author.objects.all()
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")

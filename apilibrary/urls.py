from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter, DefaultRouter

from apilibrary.views import BooksViewSet, GenresViewSet, BookCommentsViewSet, AuthorsViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')
router.register('genres', GenresViewSet, basename='genres')
router.register('authors', AuthorsViewSet, basename='authors')

book_comments_router = NestedSimpleRouter(router, 'books', lookup='book')
book_comments_router.register('comments', BookCommentsViewSet, basename='book-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_comments_router.urls)),
]

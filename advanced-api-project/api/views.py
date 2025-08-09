from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework


class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter]
    # Simple exact filters (author expects id)
    filterset_fields = ['title', 'publication_year', 'author']

    # Full-text search on title and author's name
    search_fields = ['title', 'author__name']

    # Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


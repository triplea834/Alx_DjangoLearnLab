from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# List & Create (GET / POST)
class BookListViewCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']

# Retrieve / Update / Destroy (GET / PUT/PATCH / DELETE)
class BookDetailViewUpdateViewDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Example customization: show who made it (if you had an owner field)
    # def perform_update(self, serializer):
    #     serializer.save(modified_by=self.request.user)

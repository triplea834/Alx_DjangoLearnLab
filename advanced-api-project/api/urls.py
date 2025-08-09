from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

# books/create books/update books/delete

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]

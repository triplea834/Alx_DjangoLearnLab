# api/models.py
from django.db import models

class Author(models.Model):
    """
    Represents an author who can have many books.
    Fields:
    - name: full name of the author (string)
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book. Each Book belongs to one Author (ForeignKey).
    Fields:
    - title: book title
    - publication_year: year the book was published (integer)
    - author: ForeignKey to Author (one-to-many relationship)
      Note: related_name='books' makes author.books.all() available.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


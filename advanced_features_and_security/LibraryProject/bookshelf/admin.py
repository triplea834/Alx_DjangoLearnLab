from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields
    search_fields = ('title', 'author')                    # Enable search
    list_filter = ('publication_year',)                    # Filter by publication year

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)


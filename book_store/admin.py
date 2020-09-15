from django.contrib import admin

from book_store.models import Book, BookType

admin.site.register(Book)
admin.site.register(BookType)

from rest_framework.generics import (
    ListCreateAPIView,              # GET (list) + POST (create)
    RetrieveUpdateDestroyAPIView    # GET (single) + PUT/PATCH + DELETE
)

from .models import Book
from .serializers import BookSerializer


#Handles: GET all books + POST new book
class BookListCreateAPIView(ListCreateAPIView):
    """
    Combined view for:
    - GET /books/      → list all books
    - POST /books/     → create a new book
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Handles: GET one book + UPDATE + DELETE
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Combined view for:
    - GET /books/1/    → retrieve one book
    - PUT /books/1/    → full update
    - PATCH /books/1/  → partial update
    - DELETE /books/1/ → delete book
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
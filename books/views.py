from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    ViewSet that handles ALL CRUD operations:

    - GET /books/        → list all books
    - POST /books/       → create a new book
    - GET /books/1/      → retrieve single book
    - PUT /books/1/      → full update
    - PATCH /books/1/    → partial update
    - DELETE /books/1/   → delete book
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
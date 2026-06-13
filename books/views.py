from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

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

    # Only authenticated users can access
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        GET /books/recent/
        Returns the 5 most recently published books.
        """
        recent_books = Book.objects.order_by('-published_date')[:5]
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def cheapest(self, request):
        """
        GET /books/cheapest/
        Returns the cheapest book.
        """
        cheapest_book = Book.objects.order_by('price').first()

        if not cheapest_book:
            return Response(
                {"message": "No books available."},
                status=404
            )

        serializer = self.get_serializer(cheapest_book)
        return Response(serializer.data)
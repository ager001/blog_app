from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
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
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_books = Book.objects.order_by('-published_date')[:5]
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)    
    
    @action(detail=False, methods=['get'])
    def cheapest(self, request, pk=None):
        cheapest_book = Book.objects.order_by('price').first()
        serializer = self.get_serializer(cheapest_book)
        return Response(serializer.data)

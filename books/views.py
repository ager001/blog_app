from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookListAPIView(GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):

        books = self.get_queryset()

        serializer = self.get_serializer(
            books,
            many=True
        )

        return Response(serializer.data)
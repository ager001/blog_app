from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin, 
    UpdateModelMixin
)
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(
    ListModelMixin,
    CreateModelMixin,
    GenericAPIView,
    
):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # GET /books/
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # POST /books/
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
    
class BookDetailAPIView(
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericAPIView
):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # GET /books/1/
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # DELETE /books/1/
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    # PATCH /books/1/
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
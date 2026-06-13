from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.views import APIView
from django.contrib.auth.models import User


from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # 🔐 Default: only logged-in users can view
    permission_classes = [IsAuthenticated]
    
     # 👇 Override permissions for unsafe actions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_books = Book.objects.order_by('-published_date')[:5]
        serializer = self.get_serializer(recent_books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def cheapest(self, request):
        cheapest_book = Book.objects.order_by('price').first()
        serializer = self.get_serializer(cheapest_book)
        return Response(serializer.data)
    

class SuperUserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.filter(is_superuser=True)

        data = [
            {
                "username": user.username,
                "email": user.email,
                "is_staff": user.is_staff,
                "date_joined": user.date_joined
            }
            for user in users
        ]

        return Response(data)    
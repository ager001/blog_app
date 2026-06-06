from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author','price']
        
    
    def validate_title(self, value):

         title = attrs.get('title')
         author = attrs.get('author')
         price = attrs.get('price')

         if price <= 0:
          raise serializers.ValidationError("Price must be greater than zero")

         if title == author:
          raise serializers.ValidationError("Title and author cannot be the same")

         return attrs    
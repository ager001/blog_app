from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price']

    # ✅ Field-level validation (ONLY title)
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        return value

    # ✅ Field-level validation (price)
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value

    # ✅ Object-level validation (multiple fields)
    def validate(self, attrs):
        title = attrs.get('title')
        author = attrs.get('author')

        if title == author:
            raise serializers.ValidationError(
                "Title and author cannot be the same"
            )

        return attrs
from rest_framework import serializers
from .models import Book, Publisher



class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    
    publisher_detail = PublisherSerializer(source='publisher', read_only=True)
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'publisher', 'publisher_detail']

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
        title = attrs.get('title', getattr(self.instance, 'title', None))
        author = attrs.get('author', getattr(self.instance, 'author', None))

        if title == author:
            raise serializers.ValidationError(
                "Title and author cannot be the same"
            )

        return attrs
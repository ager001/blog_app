from rest_framework import serializers
from .models import Book, Publisher, Author



class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name','email']
        
        

class BookSerializer(serializers.ModelSerializer):
    
    # 🔵 READ: full nested objects
    author_detail = AuthorSerializer(source='author', read_only=True)
    publisher_detail = PublisherSerializer(source='publisher', read_only=True)
    
    
    # 🟢 WRITE: only IDs
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True
    )
    
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'publisher', 'publisher_detail', 'author_detail']

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

   
    def validate(self, attrs):
      title = attrs.get('title')

      if Book.objects.filter(title=title).exists():
        raise serializers.ValidationError("Book with this title already exists")

      return attrs
  
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = {
            'name': instance.author.name if instance.author else None,
            'email': instance.author.email if instance.author else None
        }
        representation['publisher'] = {
            'name': instance.publisher.name if instance.publisher else None,
            'address': instance.publisher.address if instance.publisher else None,
        }
        return representation
    
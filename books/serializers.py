from rest_framework import serializers
from .models import Book, Publisher, Author


# Publisher Serializer
class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'email']


# Book Serializer
class BookSerializer(serializers.ModelSerializer):

    #READ ONLY: full nested representation
    author_detail = AuthorSerializer(source='author', read_only=True)
    publisher_detail = PublisherSerializer(source='publisher', read_only=True)

    # WRITE ONLY: IDs for clean API input
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True
    )

    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        write_only=True
    )
    
    published_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'category',
            'price',

            # write fields
            'author',
            'publisher',

            # read fields
            'author_detail',
            'publisher_detail',
            'published_date',
        ]

    # VALIDATION

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value

    def validate(self, attrs):
        title = attrs.get('title')

        # Better approach assumes DB-level uniqueness is NOT enforced
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError(
                "Book with this title already exists"
            )

        return attrs
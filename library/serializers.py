from rest_framework import serializers

from library.models import Book, Writer


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        read_only_fields = ('id',)
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    owner = WriterSerializer ()

    class Meta:
        model = Book
        read_only_fields = ('id',)
        fields = ['id', 'name_book', 'owner']
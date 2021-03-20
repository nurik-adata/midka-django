from rest_framework import serializers
from apps.models import BookJournalBase, Book, Journal

class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = ('name', 'price', 'description', 'created_at')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'created_at','num_pages', 'genre')

class JournalSerializer(serializers.ModelSerializer):
    type = serializers.ChoiseField(choices=type.objects.values_list())
    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'created_at','type', 'publisher')
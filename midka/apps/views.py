from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response  

from apps.models import BookJournalBase, Book, Journal
from apps.serializers import BookJournalBaseSerializer, BookSerializer, JournalSerializer

class BookViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class JournalViewSet (viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
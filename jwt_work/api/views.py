from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import MainContent
from .models import Tag

from .serializers import MainContentSerializer
from .serializers import TagSerializer

from rest_framework.permissions import IsAuthenticated

class MainContentViewSet(viewsets.ModelViewSet):
    queryset = MainContent.objects.all()
    serializer_class = MainContentSerializer

    #認証済みのみアクセス可能
    permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    #認証済みのみアクセス可能
    permission_classes = [IsAuthenticated]
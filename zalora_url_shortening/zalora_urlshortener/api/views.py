from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import ShortenerSerializer
from zalora_urlshortener.models import Shortener

# Create your views here.
class ListShortenerAPIView(ListAPIView):
    """This endpoint list all of the available Shorteners from the database"""
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer

class CreateShortenerAPIView(CreateAPIView):
    """This endpoint allows for creation of a Shortener"""
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer

class UpdateShortenerAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Shortener by passing in the id of the Shortener to update"""
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer

class DeleteShortenerAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Shortener from the database"""
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer

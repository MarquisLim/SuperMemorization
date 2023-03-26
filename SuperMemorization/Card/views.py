from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class CardAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
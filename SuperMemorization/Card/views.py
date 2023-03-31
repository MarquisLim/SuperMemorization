from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from .filters import UsersFitler
from django_filters import rest_framework as rest_filters
from django.urls import path
from django.shortcuts import render
from . import views
from django_filters.rest_framework import DjangoFilterBackend

class CardAPIView(APIView):

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(Card, many=True)
        return Response(serializer.data)

    def post(self, request):
        card = CardSerializer(data=request.data)
        if card.is_valid():
            card.save()
        return Response(status=201)


class DeckAPIView(APIView):
    def get(self, request):
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)

    def post(self, request):
        deck = DeckSerializer(data=request.data)
        if deck.is_valid():
            deck.save()
        return Response(status=201)


class DeckDetailAPIView(APIView):

    def patch(self, request, id):
        deck = Deck.objects.get(id=id)
        data = request.data
        deck.title = data.get('title', deck.title),
        deck.description = data.get('description', deck.description)
        deck.save()
        serializer = DeckSerializer(deck)
        return Response(serializer.data, status=200)

    def delete(self, request, id):
        deck = Deck.objects.get(id=id)
        deck.delete()
        return Response('Удален')


class CardDetailAPIView(APIView):

    def patch(self, request, id):
        card = Card.objects.get(id=id)
        data = request.data
        card.front = data.get('front', card.front)
        card.back = data.get('back', card.back)
        card.image = data.get('image', card.image)
        card.save()
        serializer = DeckSerializer(card)
        return Response(serializer.data, status=200)

    def delete(self, яrequest, id):
        deck = Deck.objects.get(id=id)
        deck.delete()
        return Response('Удален')




class DecksOfUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = DecksOfUserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['username', 'decks__title']
    filterset_class = UsersFitler

    #  filter_backends = [rest_filters.DjangoFilterBackend]
    # filterset_fields = '__all__'
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)


def index(request):
    context = {}
    return render(request, 'index.html', context)


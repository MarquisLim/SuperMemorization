from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView



class CardAPIView(APIView):

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
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

    def get(self, request, id):
        deck = Deck.objects.get(id=id)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)

    def patch(self, request, id):
        deck = Deck.objects.get(id=id)
        data = request.data
        deck.title = data.get('title', deck.title)
        deck.description = data.get('description', deck.description)
        deck.save()
        serializer = DeckSerializer(deck, partial=True)

        return Response(serializer.data, status=200)

    def delete(self, request, id):
        deck = Deck.objects.get(id=id)
        deck.delete()
        return Response('Удален')


class CardDetailAPIView(APIView):
    def get(self, request, id):
        card = Card.objects.get(id=id)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def patch(self, request, id):
        card = Card.objects.get(id=id)
        data = request.data
        card.front = data.get('front', card.front)
        card.back = data.get('back', card.back)
        card.image = data.get('image', card.image)
        card.save()
        serializer = DeckSerializer(card)
        return Response(serializer.data, status=200)

    def delete(self, request, id):
        deck = Deck.objects.get(id=id)
        deck.delete()
        return Response('Удален')



class DecksAPIView(APIView):
    def get(self, request):
        deck = Deck.objects.filter(user_id=request.user.id)
        print(request.user)
        serializer = CardsInDeckSerializer(deck, many=True)
        return Response(serializer.data)


class AnswerToCard(APIView):
    def post(self, request, id):
        serializer = AnswerToCardSerializer(data=request.data)
        if serializer.is_valid():
            mark = serializer.data['mark']
        card = Card.objects.get(id=id)
        card.next_review(mark)
        return Response('ok')


class RegisterAPIView(APIView):
    def post(self, request):
        user = RegisterSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response('user создан', status=201)




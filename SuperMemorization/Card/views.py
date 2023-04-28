from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.generics import ListCreateAPIView
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated


class CardAPIView(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        card = CardSerializer(data=request.data)
        if card.is_valid():
            card.save()
        return Response(status=201)
#    def perform_create(self, card):
#        card.save(user_id=self.request.user.id)

class DeckListCreateView(ListCreateAPIView):
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Deck.objects.filter(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, user):
        serializer.save(user=user)

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
        return Response(user.data, status=201)

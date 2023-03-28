from rest_framework import serializers
from .models import *
from datetime import date


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class CardListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['front', 'back', 'image', 'deck_id']
    # queryset = Card.objects.filter(next_review_date=date.today())


class CardsInDeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = ['title', 'cards']


class DecksOfUserSerializer(serializers.ModelSerializer):
    decks = CardsInDeckSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'decks']

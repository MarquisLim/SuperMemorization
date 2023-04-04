from rest_framework import serializers
from .models import *
from datetime import date


class CurrentCardSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, instance):
        if instance.next_review_date == date.today():
            return super().to_representation(instance)
        return None


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = Deck
        fields = ['id', 'title', 'description']


class CardsInDeckSerializer(serializers.ModelSerializer):
    cards = CurrentCardSerialzier(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = ['title', 'cards']


class AnswerToCardSerializer(serializers.Serializer):
    mark = serializers.IntegerField()

from rest_framework import serializers
from .models import *
from datetime import date


class CurrentCardSerialzier(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = ['id', 'front', 'back', 'image_url', 'deck_id', 'ef', 'interval', 'last_review_date', 'next_review_date']


    def to_representation(self, instance):
        if instance.next_review_date <= date.today():
            return super().to_representation(instance)
        return None
    def get_image_url(self, obj):
        if obj.image:
            return f'https://marquislim2.pythonanywhere.com/media/{obj.image}'
        return None






class  CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'front', 'back', 'deck_id', 'ef', 'interval', 'last_review_date', 'next_review_date', 'image']


class DeckSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    class Meta:
        model = Deck
        fields = ['id', 'title', 'description', 'user_id']



class CardsInDeckSerializer(serializers.ModelSerializer):
    cards = CurrentCardSerialzier(many=True, read_only=True)

    class Meta:
        model = Deck
        fields = ['title', 'description' , 'cards']


class AnswerToCardSerializer(serializers.Serializer):
    mark = serializers.IntegerField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


from django.contrib import admin
from django.urls import path
from .views import CardAPIView, DeckAPIView, DeckDetailAPIView, DecksOfUser, CardDetailAPIView, index, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls), # админ панель
    path('card/', CardAPIView.as_view()), # список и создание карточек
    path('deck/', DeckAPIView.as_view()), # список и создание колод
    path('deck/<int:id>/', DeckDetailAPIView.as_view()), # patch и delete колоды
    path('card/<int:id>/', CardDetailAPIView.as_view()),  # patch и delete карточки
    path('users/decks/cards', DecksOfUser.as_view()), # Список юзеров их колод и карты этих колод
    
]

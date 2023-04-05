from django.urls import path, include, re_path
from .views import CardAPIView, DeckAPIView, DeckDetailAPIView, CardDetailAPIView, DecksAPIView, AnswerToCard
from rest_framework_simplejwt import views
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('Это апи'), name='home'),
    path('cards/', CardAPIView.as_view()),  # список и создание карточек
    path('decks/', DeckAPIView.as_view()),  # список и создание колод 
    path('deck/<int:id>/', DeckDetailAPIView.as_view()),  # patch и delete колоды
    path('card/<int:id>/', CardDetailAPIView.as_view()),  # patch и delete карточки
    path('user/decks/', DecksAPIView.as_view()),
    path('user/answer/<int:id>', AnswerToCard.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path, include, re_path
from .views import CardAPIView, DeckAPIView, DeckDetailAPIView, CardDetailAPIView, DecksAPIView, AnswerToCard
from rest_framework_simplejwt import views
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('Это апи'), name='home'),
    path('api/v1/cards/', CardAPIView.as_view()),  # список и создание карточек
    path('api/v1/decks/', DeckAPIView.as_view()),  # список и создание колод
    path('api/v1/deck/<int:id>/', DeckDetailAPIView.as_view()),  # patch и delete колоды
    path('api/v1/card/<int:id>/', CardDetailAPIView.as_view()),  # patch и delete карточки
    path('ap1/v1/user/decks/', DecksAPIView.as_view()),
    path('api/v1/user/answer/<int:id>', AnswerToCard.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.authtoken')),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]

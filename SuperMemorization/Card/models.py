from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class Deck(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Колода'
        verbose_name_plural = 'Колоды'


class Card(models.Model):
    front = models.CharField(max_length=100, verbose_name='Термин')
    back = models.CharField(max_length=200, verbose_name='Определение')
    ef = models.FloatField(default=2.5)
    interval = models.IntegerField(default=1)
    image = models.ImageField(upload_to='IMG', blank=True, verbose_name='Изображение')
    last_review_date = models.DateField(default=datetime.now().date, verbose_name='Последняя дата провверки')
    next_review_date = models.DateField(default=datetime.now().date, verbose_name='Следующая дата проверки')
    deck_id = models.ForeignKey('Deck', on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return self.front

    def next_review(self, quality):
        # Calculate EF
        if quality < 3:
            self.ef = max(1.3, self.ef - 0.2)
        else:
            self.ef = min(2.5, self.ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        self.interval = 1 if quality < 3 else 2
        # Calculate interval
        if self.interval == 1:
            self.next_review_date = self.last_review_date + timedelta(days=1)
        else:
            self.next_review_date = self.last_review_date + timedelta(days=self.interval) * self.ef
        self.last_review_date = datetime.now()
        self.save()

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'


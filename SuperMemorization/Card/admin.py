from django.contrib import admin
from .models import *

admin.site.register(Card)


admin.site.register(Deck)

admin.site.index_title = "Добро пожаловать в интерфейс администратора Anki!"

admin.site.site_header = "Административная панель лучшего приложения Anki"

admin.site.site_title = "Админ панель"
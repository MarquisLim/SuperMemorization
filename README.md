Установка poetry — это аналог npm
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

в директории с poetry.lock нужно прописать poetry install

после установок всех зависимостей в директории, где расположен файл manage.py прописать следующую команду: 

poetry run python manage.py runserver


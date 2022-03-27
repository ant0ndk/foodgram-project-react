# Foodgram
## Удобный сервис для обмена рецептами самых разных блюд со всего мира!

## Установка на локальную машину
Создайте файл и заполните файл *.env* в */backend/*
```sh
SECRET_KEY=
DEBUG=False
ALLOWED_HOSTS=*
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=bd
DB_PORT=5432
```

Запустите docker из папки infra:
```sh
docker-compose up -d
```
И настройте проект:
```sh
docker-compose exec backend python manage.py loaddata data/fixtures.json
```
```sh
docker-compose exec backend python manage.py createsuperuser
```

Импорт ингредиентов из json:
```sh
docker-compose exec backend python manage.py load_ingredients
```

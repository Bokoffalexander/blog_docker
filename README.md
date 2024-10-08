﻿# drf_blog 

Python 3.11.5

Django==5.0.7

djangorestframework==3.15.2


# Мой готовый сервер:

Можно перейти и посмотреть

http://109.71.247.68:8008/api/v1/bloglist/

http://109.71.247.68:8008/api/v1/schema/swagger-ui/

# Запуск локально через Docker:

Делал на Ubuntu, поэтому <b>docker compose</b> у меня без тире.

1) docker build .

2) docker pull postgres:12-bullseye

3) cp env.example .env

4) docker compose up -d

5) docker exec -it blog_docker-web-1 python3 manage.py migrate

6) docker exec -it blog_docker-web-1 python3 manage.py createsuperuser (юзер: admin и пароль: admin)

7) docker exec -it blog_docker-web-1 python3 manage.py test

(Этой командой тесты запускаются от юзера: admin и паролем: admin )

# Описание:

## 1. Блог API: ->JSON и <-JSON

## 2. БД postgresql

## 3. Описание ручек

### (А) GET и POST  - IsAuthenticatedOrReadOnly

#### Авторизация Basic 

http://localhost:8008/api/v1/bloglist/

### (Б) PATCH и DELETE - Owner или Admin

#### Авторизация Basic

http://localhost:8008/api/v1/bloglist/<int:pk>/

### (В) Ручки-OpenAPI

http://localhost:8008/api/v1/schema/

#### Чтобы авторизоваться в Swagger, нужно logout из DRF-Browsable-API

http://localhost:8008/api/v1/schema/swagger-ui/

http://localhost:8008/api/v1/schema/redoc/

### (Г) Необязательная ручка

#### Получить список юзеров (без сериализации) - ответ JSON

#### Авторизация Token 

http://localhost:8008/api/v1/listusers/

GET [permissions.IsAdminUser] + [authentication.TokenAuthentication]

## 4. Описание ERRORS - Возвращается json ответ ошибки:

1) Для данного URL нет такого метода

return Response({"error": "Method PATCH not allowed"})

2) Объекта с таким pk не существует

return Response({"error": "Object does not exists"})

3) Неверный json, то вернет ответ: поле обязательно

serializer.is_valid(raise_exception=True)

4) Не владелец, и не Админ пытается изменить запись

return Response({"error": "You can't PATCH this obj, isn't yours."})

5) Не владелец, и не Админ пытается удалить запись

return Response({"error": "You can't DElETE this obj, isn't yours."})


## 5. Сериализатор

наследует от ModelSerializer

## 6. Представление

наследует от APIView

## 7. Добавил login-Browsable-API (в браузере)

## 8. Тесты:

### Есть команда через докер (в начале описано)

### Запускаются после runserver

Использовал: TestCase и requests

Проверка:

GET и POST '/api/v1/bloglist/'

PATCH и DELETE '/api/v1/bloglist/<int:pk>/'

#### 9. Для ручной отправки запросов использовал - python, а не Postman

#### Файл request.py (request-JSON и response-JSON)

```

import requests
import json

#### для GET и POST - IsAuthenticatedOrReadOnly
url1 = "http://localhost:8008/api/v1/bloglist/"

#### для PATCH и DELETE - Owner или Admin
url2 = "http://localhost:8008/api/v1/bloglist/120/"

#### для GET - IsAdminUser + Token
url3 = "http://localhost:8008/api/v1/listusers/"

payload = {"title":"Hi python",  "content": "any", "is_published": "true"}
json_payload = json.dumps(payload, indent = 4) 

# Авторизация-Basic логин:пароль - затем энкод BASE64
# admin:admin YWRtaW46YWRtaW4=
# user2:Olordjesus dXNlcjI6T2xvcmRqZXN1cw==
# user3:Hiscross dXNlcjM6SGlzY3Jvc3M=
# только для url1 и url2.
headers12 = {"Authorization":"Basic YWRtaW46YWRtaW4=", 'Content-Type': 'application/json'}

# Авторизация-Token
#admin ccf390f60e6016f26dcebcaab33c7ee644ea7319
# только для url3.
headers3 = {"Authorization":"Token ccf390f60e6016f26dcebcaab33c7ee644ea7319"}

response = requests.request("PATCH", url2, headers=headers12, data=json_payload)

print(response.text)
print(response.status_code)


```

# drf_blog

# Мой готовый сервер:

Можно перейти и посмотреть

http://109.71.247.68:8008/api/v1/bloglist/

# Запуск через Docker:

1) docker build .

2) docker pull postgres:12-bullseye

3) docker compose up -d

4) docker exec -it blog_test_openapi-web-1  python3 manage.py
migrate

5) docker exec -it blog_test_openapi-web-1  python3 manage.py createsuperuser (admin : admin)

6) docker exec -it blog_test_openapi-web-1  python3 manage.py
test (если нужны тесты, там запросы от юзера: admin и паролем: admin )

# Описание:

## 1. Блог API: ->JSON и <-JSON

## 2. БД postgresql

## 3. Описание ручек

### (А) GET и POST  - IsAuthenticatedOrReadOnly

#### Авторизация Basic 

localhost:8008/api/v1/bloglist/

### (Б) PATCH и DELETE - Owner или Admin

#### Авторизация Basic

localhost:8008/api/v1/bloglist/<int:pk>/

### (В) Ручки-OpenAPI

localhost:8008/api/v1/schema/

#### Чтобы авторизоваться в Swagger, нужно logout из DRF-Browsable-API

localhost:8008/api/v1/schema/swagger-ui/

localhost:8008/api/v1/schema/redoc/

### (Г) Необязательная ручка

#### Получить список юзеров (без сериализации) - ответ JSON

#### Авторизация Token 

localhost:8008/api/v1/listusers/

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

### запустить после runserver

python manage.py test

Проверка:

Использовал: TestCase и requests

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
#admin 86d9dc6568afeecc35403ed54fe59ae4b2faf2db
# только для url3.
headers3 = {"Authorization":"Token 86d9dc6568afeecc35403ed54fe59ae4b2faf2db"}

response = requests.request("PATCH", url2, headers=headers12, data=json_payload)

print(response.text)
print(response.status_code)


```

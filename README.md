# drf_blog

# Описание:

## Блог API: ->JSON и <-JSON

## Пока на sqlite

## Описание ручек

### GET и POST  - IsAuthenticatedOrReadOnly

#### Авторизация Basic 

'/api/v1/bloglist/'

### PATCH и DELETE - Owner или Admin

#### Авторизация Basic

'/api/v1/bloglist/<int:pk>/'

### Ручки-OpenAPI

OpenAPI 'api/v1/schema/'

#### Чтобы авторизоваться в Swagger, нужно logout из DRF-Browsable-API

OpenAPI 'api/v1/schema/swagger-ui/'

OpenAPI 'api/v1/schema/redoc/'

#### Необязательная ручка

#### Получить список юзеров (без сериализации) - ответ JSON

#### GET - Admin+Token

##### Авторизация Token 

1) [permissions.IsAdminUser] 

2) [authentication.TokenAuthentication]

'api/v1/listusers/'

## Описание ERRORS - Возвращается json ответ ошибки:

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


## Сериализатор

наследует от ModelSerializer

## Представление

наследует от APIView

## Добавил login-Browsable-API (в браузере)

## Тесты:

### запустить после runserver

python manage.py test

Проверка:

Использовал: TestCase и requests

GET и POST '/api/v1/bloglist/'

PATCH и DELETE '/api/v1/bloglist/<int:pk>/'

#### Для ручной отправки запросов использовал - python, а не Postman

#### Файл request.py (request-JSON и response-JSON)

```

import requests
import json

#### для GET и POST - IsAuthenticatedOrReadOnly
url1 = "http://localhost:8000/api/v1/bloglist/"

#### для PATCH и DELETE - Owner или Admin
url2 = "http://localhost:8000/api/v1/bloglist/120/"

#### для GET - IsAdminUser + Token
url3 = "http://localhost:8000/api/v1/listusers/"

payload = {"title":"Hi python",  "content": "any", "is_published": "true"}
json_payload = json.dumps(payload, indent = 4) 

# Авторизация-Basic логин:пароль - затем энкод BASE64
# admin:admin YWRtaW46YWRtaW4=
# user2:Olordjesus dXNlcjI6T2xvcmRqZXN1cw==
# user3:Hiscross dXNlcjM6SGlzY3Jvc3M=
# только для url1 и url2.
headers12 = {"Authorization":"Basic YWRtaW46YWRtaW4=", 'Content-Type': 'application/json'}

# Авторизация-Token
#admin 65b6ca5f54722ae63ceef8b8941b0aafd329070b
#user2 41faaf22cd83f35ad5edce2c08e4a61457e9eff9
#user3 aacab635ebaa5ae7f703e53c6494f0ae35933ef8
# только для url3.
headers3 = {"Authorization":"Token 65b6ca5f54722ae63ceef8b8941b0aafd329070b"}

response = requests.request("PATCH", url2, headers=headers12, data=json_payload)

print(response.text)
print(response.status_code)


```

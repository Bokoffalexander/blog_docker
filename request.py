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
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
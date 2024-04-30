import requests
import json

# Настройка URL
url = 'http://45.135.233.242:8001/auth/login'

# Настройка шапки

headers ={
    'content-type': 'application/json',
    'authorization': 'Berrer your_token'
}

#Set up the request body

payload ={
    'email': 'qwerty@mail.ru',
    'password': '12345'
}

json_payload = json.dumps(payload)

#Make the POST request

response = requests.post(url=url, data=json_payload)
print(response)
if response.status_code <=204:
    print('Подключение установлено!')
    print(response.json())
else:
    print('Ошибка подключения!')
    print(response.text)

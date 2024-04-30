import requests
#
# URL = f"https://robotfastapi.digitalberd.com/"
#
# r = requests.get(url=URL)
# result = r.json()
#
# if r.status_code == 200:
#
#     print(result)
#     print(type(result))
#     print(r.text)
#     print(r.status_code)
#     print(result.get('data'))
# else:
#     print('Was ERROR!!!')



curr = 'USD,GBP,EUR'
import datetime
start_data ='01-01-2023'
end_data = '31-12-2023'
sd = datetime.datetime.strptime(f'{start_data}', '%d-%m-%Y')
ed = datetime.datetime.strptime(f'{end_data}', '%d-%m-%Y')
URL = f'https://www.cbr-xml-daily.ru/archive/{sd.year}/{sd.month:02d}/{sd.day:02d}/daily_json.js'
r = requests.get(url=URL)
result = r.json()
print(result)
print(result.get("Valute").get("USD").get('CharCode'), result.get("Valute").get("USD").get('Value'))
print(result.get("Valute").get("EUR").get('CharCode'), result.get("Valute").get("EUR").get('Value'))
import json

json_1 = json.dumps(result, indent=4)

# print(json_1 )

import requests

import pandas as pd

csv_file = pd.DataFrame(None, columns=['Data', 'Valuta', 'Kurs'])
csv_file.to_csv('spisok_valut.csv', index=False)
a = pd.date_range(start='03/01/2024', end='04/01/2024')
for i in a:
    try:
        URL = f'https://www.cbr-xml-daily.ru/archive/{i.year}/{i.month:02d}/{i.day:02d}/daily_json.js'
        r = requests.get(url=URL)
        result = r.json()
        spisok_valut = [{
            "Data": f'{i.year}-{i.month:02d}-{i.day:02d}',
            "Valuta": result.get("Valute").get("USD").get('CharCode'),
            "Kurs": result.get("Valute").get("USD").get('Value')
        }]
        result1 = result
    except AttributeError:
        spisok_valut = [{
            "Data": f'{i.year}-{i.month:02d}-{i.day:02d}',
            "Valuta": result1.get("Valute").get("USD").get('CharCode'),
            "Kurs": result1.get("Valute").get("USD").get('Value')
        }]
    print(spisok_valut)
    csv_file = pd.DataFrame(spisok_valut)
    csv_file.to_csv('spisok_valut.csv', mode='a', index=False, header=False)




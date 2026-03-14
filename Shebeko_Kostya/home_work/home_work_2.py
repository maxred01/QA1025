import requests

URL = "https://httpbin.org/post" #URL сайта

data = {'Ruin': 'Ruin2333', '5476ruin': 'qwerty'} #Данные для отравки через POST

try: #Используем try для того,чтобы код продолжился, если возникнет ошибка. После напишет, какая ошибка
    response = requests.post(url=URL, data=data) #Используем метод POST
    response.raise_for_status()#Проверяем статус
    result = response.json()#Выводим результат в json
    print(result.get('form'))#Пишем ответ

except requests.exceptions.HTTPError:#Выводит при ошибке статус кода
    print(f"Ошибка: {response.status_code}")
except requests.exceptions.ConnectionError:#Выводит при ошибке соединение
    print(f"Сервер недоступен: {response.status_code}")

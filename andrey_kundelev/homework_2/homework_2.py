# Задание
# Отправьте GET-запрос на https://httpbin.org/json.
# Извлеките значение поля slideshow.title из ответа.
# Выведите результат в формате:
# Title: [НАЙДЕННЫЙ_ЗАГОЛОВОК]

import requests

response = requests.get('https://httpbin.org/json')
print(response.status_code)  # Код статуса (200 = OK)
data = response.json()
title = data["slideshow"]["title"]
print(f'Title: {title}')     # Ответ в формате JSON


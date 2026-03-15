import requests

URL = "https://httpbin.org/json" #URL сайта

response = requests.get(URL)

print(response.status_code)  #Код ответа сайта

data = response.json() # Ответ преобразуется в json файл

title = data['slideshow']['title'] # Здесь извлекаем значение поля

print(f"Title: {title}") #Выводим результат



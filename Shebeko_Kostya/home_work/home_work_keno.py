import requests
from collections import Counter

from Shebeko_Kostya.home_work.helpers_keno.helpers_keno_curl import keno_curl

url = "https://sportpari.by/api/game/2/draw-results"

querystring = {"filter_results_type":"draw_date","draw_date":"{\"start\":\"2026-3-8\",\"end\":\"2026-4-7\"}","page":"1"}

response = requests.request("GET", url, headers=keno_curl, params=querystring)

data = response.json()

all_numbers = []

draws = data.get('draw_results', [])

for draw in draws:
    numbers = draw.get('results', [])
    all_numbers.extend(numbers)
if all_numbers:
    counts = Counter(all_numbers)
    print('Топ-10 чисел в КЕНО')
    print("Число - Сколько раз выпало")
    for number, freq in counts.most_common(10):
        print(f'{number:1} - {freq:1}')







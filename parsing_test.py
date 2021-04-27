'''
import requests
from bs4 import BeautifulSoup

r = requests.get('https://smekm.ru/pinta_feed.xml')
if r.status_code == 200:
    soup = BeautifulSoup(r.text)
    print(soup)
else:
    r.raise_for_status()
'''


from parsing import yandex_id, google_id

google_id = google_id('https://smekm.ru/pinta_feed.xml')
yandex_id = yandex_id('https://smekm.ru/yml_get/ctfjm41hwzr')

crossing_id = []

for i in yandex_id:
    for j in google_id:
        if i == j:
            crossing_id.append(i)

print(len(crossing_id))
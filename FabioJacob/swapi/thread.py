import requests
import threading
import time

base_url = 'https://swapi.co/api/people/?search=skywalker'


def get_urls():
    movies = requests.get(base_url).json()['results'][0]['films']
    return movies

def get_movies_name():
    mn = []
    for url in get_urls():
        film = requests.get(url).json()
        mn.append(film['title'])
    mn.sort()

    return mn

t0 = time.time()
th1 = threading.Thread(target=get_movies_name)
th2 = threading.Thread(target=get_movies_name)
th3 = threading.Thread(target=get_movies_name)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()

# get_urls()
# names = get_movies_name()
# print(names)
t1 = time.time()

print(f'tempo: {t1 - t0:.2f}s')
import time
import requests
from bs4 import BeautifulSoup
import os
import re
import io

# tworzneie listy do sczytania wszystkich linków do stron z autorami wierszy
# lista przejdzie po wszystkich stronach i dla nich pobierze linki do autorow i zapisze je
page_list =["https://pl.wikisource.org/wiki/Kategoria:Polscy_poeci",
           "https://pl.wikisource.org/w/index.php?title=Kategoria:Polscy_poeci&pagefrom=Laskowski%2C+Kazimierz%0AKazimierz+Laskowski#mw-pages",
           "https://pl.wikisource.org/w/index.php?title=Kategoria:Polscy_poeci&pagefrom=Wolski%2C+Wac%C5%82aw%0AWac%C5%82aw+Wolski#mw-pages"]

url_autors = []

start = time.time()

for page_url in page_list:
    # określenie strony do szukania linków z autorami
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        if a['href'][0:11] == '/wiki/Autor':
            url_autors.append(a['href'])

print(f'Udało mi się pobrać {len(url_autors)} autorów w ciągu {round(time.time() - start, 1)} sekund')

i = 1  # iteracja kolejnych autorów
start_full = time.time()

for url_autor in url_autors[0:10]:
    start = time.time()
    autor = url_autor.replace('/wiki/Autor:', '')

    # tutaj tworzy się folder autora (jeśli jeszcze nie istnieje)
    directory = f'./data_raw/{autor}/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    url = 'https://pl.m.wikisource.org' + url_autor.replace('Autor', 'Kategoria')
    # ta zmiana sprawia, że prościej odczytuje się stronę
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        # znalezienie wierszy ze strony autora
        poems_url = []
        for a in soup.find_all('a', href=True):
            if '/wiki/Autor:' not in a['href'] and '/wiki/Kategoria:' not in a['href']:
                poems_url.append(a['href'])

        # przycięcie tylko do tekstów i pozbycie się zbędnych linków
        list_index_from = [idx for idx, s in enumerate(poems_url) if '&from=%C5%BB' in s][0]
        poems_url = poems_url[list_index_from + 1:]

        poems_url = [poems for poems in poems_url if '/w/index.php?title=Kategoria:' not in poems]

        list_index_to = [idx for idx, s in enumerate(poems_url) if '/wiki/' not in s][0]
        poems_url = poems_url[:list_index_to]
    except:
        pass
        # pętla do pobrania wszystkich znalezionych wierszy z url
    for poem in poems_url:
        title = poem.replace('/wiki/', '')

        try:
            page = requests.get('https://pl.m.wikisource.org' + poem)
            soup = BeautifulSoup(page.content, 'html.parser')
            # zamiana break lines na nową linie
            for br in soup.find_all("br"):
                br.replace_with("\n")
            # szukanie tekstu
            text = soup.find_all('p').get_text()
            # czyszczenie
            clean_text = re.sub('<.*?>', '', str(text))
            # usunięcie elementów html znajdujacych sie między znakami < oraz >
            # zapisanie pliku
            with io.open(directory + title.replace('/', ' ') + '.txt', "w", encoding="utf-8") as f:
                f.write(str(clean_text))
        except:
            pass
    print(
        f'Autor {i} z {len(url_autors)}: {autor}; pobrano {len(poems_url) - 1} dzieł w ciągu {round(time.time() - start, 1)} sekund')
    print(url)
    i = i + 1

print(f'Całość zajęła {round(time.time() - start_full, 1)} sekund')

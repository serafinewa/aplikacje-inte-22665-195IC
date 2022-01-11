from bs4 import BeautifulSoup
import requests
import csv

#pobranie strony http://coreyms.com jako źródło do scrape'owania
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape_one.csv', 'w')
# pobrane informacje beda zapisane w pliku scrape_one
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
# metoda find_all wyodrębnia pojedynczy tag i znajdzie wszystkie jego wystąpienia na stronie.
# z użyciem tej samej metody można zbadać konkretną klasę lub identyfikator na stronie
# wypisanie dla klasy article naglowkow na stronie
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
# wypisanie zawartosci klasy entry-content na stronie
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
        # exception jezeli nie ma linku na youtube
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()
# wypisanie naglowka, tekstu na stronie i linka do filmu na youtube
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

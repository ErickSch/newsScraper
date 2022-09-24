# https://www.nytimes.com/international/

from bs4 import BeautifulSoup
import requests


url = 'https://www.nytimes.com/international/?action=click&region=Editions&pgtype=Homepage'
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, features="html")
headers = soup.find_all('h3')

for i in range(len(headers)):
    h3 = str(headers[i])
    h3 = h3.split('<')
    h3 = h3[1].split('>')
    headers[i] = h3[1]

# Insert key words
words = ['falls', 'fall', 'low', 'crisis', 'sell']
headers_words = []

for h in headers:
    for w in words:
        if w in h:
            headers_words.append(h)


for n in headers_words:
    print(n)



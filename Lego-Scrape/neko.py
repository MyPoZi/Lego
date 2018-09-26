import requests
from bs4 import BeautifulSoup

URL = 'http://gihyo.jp/lifestyle/clip/01/everyday-cat'

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
# title = soup.title
# print(type(title))
# print(title)

div = soup.find('div', class_='readingContent01')
# li = div.find('li')
# print(li.a['href'])
#
# print(li.a.text)
for li in div.find_all('li'):
    url = li.a['href']
    date, text = li.a.text.split(maxsplit=1)
    print('{},{},{}'.format(date, text, url))

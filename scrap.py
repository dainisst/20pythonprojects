import requests
from bs4 import BeautifulSoup

url = 'https://www.lsm.lv/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('span', {'class': 'thumbnail__caption_text'})

print(title)

# title1 = title[0].getText()
# print(title1)
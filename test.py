from app.naointendo import NaoIntendo
from bs4 import BeautifulSoup
import requests

r = requests.get('http://feeds.feedburner.com/naointendo')
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')

item = soup.find('item')
title = item.find('title')
print('title: ', title.text)

desc = item.find('description')

desc_soup = BeautifulSoup(desc.text, 'html.parser')
print(desc_soup)

# p = desc_soup.find('p').text
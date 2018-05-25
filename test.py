from app.naointendo import NaoIntendo
from bs4 import BeautifulSoup
import requests

r = requests.get('http://feeds.feedburner.com/naointendo')
soup = BeautifulSoup(r.text, 'html.parser')

item = soup.find('item')

desc = item.find('description')

desc_soup = BeautifulSoup(desc.text, 'html.parser')

p = desc_soup.find('p').text
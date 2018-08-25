from bs4 import BeautifulSoup
from random import randint
import json
import requests

class GoogleSearch:
    def __init__(self):
        self.url = 'https://www.google.com.br/search?hl=pt-BR&tbm=isch&source=hp&q={query}&oq={query}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
        }
    
    def get_soup(self, query):
        return BeautifulSoup(
            requests.get(self.url.format(query=query), headers=self.headers).text,
            'html.parser'
        )
    def random_image(self, query):
        soup = self.get_soup(query)
        self.links = list()
        for s in soup.find_all('div', {'class': 'rg_meta'}):
            try:
                self.links.append(json.loads(s.text)['ou'])
            except:
                continue
        return self.links[randint(0, len(self.links))]

    def random_redhead(self):
        return self.random_image(query='redhead girl')

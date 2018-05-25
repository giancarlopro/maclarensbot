from bs4 import BeautifulSoup
import requests
from random import randint

class NaoIntendo:
    def __init__(self):
        self.base_url = 'http://feeds.feedburner.com/naointendo'

    def last_post(self):
        """Returns a url for one naointendo post"""
        res = requests.get(self.base_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        for item in soup.findAll('item'):
            desc = item.find('description')
            if len(desc.text) > 0:
                img_soup = BeautifulSoup(desc.text, 'html.parser')
                try:
                    img = str(img_soup.find('img')['src']).encode('utf8')
                    p = str(img_soup.find('p').text).encode('utf8')

                    return {'img': img, 'desc': p}
                except:
                    pass

        return False
    
    def random_post(self):
        """Returns a url for one naointendo post"""
        res = requests.get(self.base_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        urls = dict()

        for i in range(20):
            itens = soup.findAll('item')
            desc = itens[i].find('description')
            if len(desc.text) > 0:
                img_soup = BeautifulSoup(desc.text, 'html.parser')
                try:
                    img = str(img_soup.find('img')['src']).encode('utf8')
                    p = str(img_soup.find('p').text).encode('utf8')

                    urls[img] = p
                except:
                    pass
        try:
            i = randint(0, len(urls.keys()))
            img = urls.keys()[i]
            p = urls[img]
            return {'img': img, 'desc': p}
        except:
            return self.last_post()
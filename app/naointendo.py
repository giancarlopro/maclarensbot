from bs4 import BeautifulSoup
import requests

class NaoIntendo:
    def __init__(self):
        self.base_url = 'http://feeds.feedburner.com/naointendo'

    def random_post(self):
        """Returns a url for one naointendo post"""
        res = requests.get(self.base_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        for item in soup.findAll('item'):
            desc = item.find('description')
            if len(desc.text) > 0:
                img_soup = BeautifulSoup(desc.text, 'html.parser')
                try:
                    img = img_soup.find('img')['src']
                    return str(img).encode('utf8')
                except:
                    pass

        return False
from BeautifulSoup import BeautifulSoup
import requests

class NaoIntendo:
    def __init__(self):
        self.base_url = 'http://feeds.feedburner.com/naointendo'

    def random_post(self):
        """Returns a url for one naointendo post"""
        res = requests.get(self.base_url)
        soup = BeautifulSoup(res.text)

        post = soup.find('item')
        img = post.find('description')

        url = str(img).split("src=\"")[1]
        url = url.split('"')[0]

        return url
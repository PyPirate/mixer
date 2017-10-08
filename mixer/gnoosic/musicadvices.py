import requests
from bs4 import BeautifulSoup
from collections import deque

class MusicAdvisor:
    gnoosic_url = 'http://www.gnoosic.com/faves.php'
    request_headers = {'Host': 'www.gnoosic.com',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Referer': 'http://www.gnoosic.com/faves.php', 'Cookie': 's=28836344',
                       'Accept-Encoding': 'gzip, deflate'
                       }

    def __init__(self, bands):
        self.bands = deque(bands)
        self._feed_initial_bands()

    def _feed_initial_bands(self):
        self.request_params = {'skip': 1, 'Fave01': self.bands[0], 'Fave02': self.bands[1], 'Fave03': self.bands[2]}

    def _mash_up_bands(self, new_band):
        self.bands.popleft()
        self.bands.append(new_band)
        self._feed_initial_bands()

    def find_new_band(self):
        response = requests.post(self.gnoosic_url, data=self.request_params, headers=self.request_headers).content
        soup = BeautifulSoup(response, 'lxml')
        return soup.find(id='result').string

    def get_multiple_bands(self, amount=7):
        def get_band():
            band = self.find_new_band()
            self._mash_up_bands(band)
            return band
        return [get_band() for i in range(amount)]

if __name__ == '__main__':
    advisor = MusicAdvisor(['Rihanna', 'Radiohead', 'Metallica'])
    print advisor.get_multiple_bands()
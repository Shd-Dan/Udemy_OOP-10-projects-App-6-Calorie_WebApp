import requests
from selectorlib import Extractor


class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage
    """
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace('', '-')

    def _build_url(self):
        """Builds url address"""
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        req = requests.get(url, headers=self.headers)
        cont = req.content
        cont = req.text
        extract = Extractor.from_yaml_file(self.yml_path)
        middle = extract.extract(cont)
        return middle

    def get(self):
        final_scrape = self._scrape()
        res = float(final_scrape['temp'].replace('°C', '').strip())
        return res


#     def get(self):
#         req = requests.get(f'https://www.timeanddate.com/weather/{self.country}/{self.city}')
#         cont = req.content
#         cont = req.text
#         extract = Extractor.from_yaml_file("temperature.yaml")
#         middle = extract.extract(cont)
#         res = float(middle['temp'].replace('\xa0°C', ''))
#         return res


temp = Temperature(country='kazakhstan', city='almaty')
print(temp.get())

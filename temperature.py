import requests
from selectorlib import Extractor


class Temperature:
    """Scraper Class to get tempoture from website"""
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = "https://www.timeanddate.com/weather/"
    yml_path = "temperature.yaml"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        c = r.text
        raw_result = extractor.extract(c)
        return raw_result

    def get(self):
        scrapped_content = self.scrape()
        return float(scrapped_content['temp'].replace("\xa0°F", ""))


# if __name__ == "__main__":
#     temperature = Temperature("usa", "nashville")
#     print(temperature.get())

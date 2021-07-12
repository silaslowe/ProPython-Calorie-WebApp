import requests
from selectorlib import Extractor


class Temperature:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def get(self):
        r = requests.get('https://www.timeanddate.com/weather/usa/nashville')
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_result = extractor.extract(c)
        result = float(raw_result['temp'].replace("\xa0°F", ""))

        print(result)

class Calorie:
    def __init__(self, height, weight):


temp = Temperature("Rome", "Italy")

print(temp.get())

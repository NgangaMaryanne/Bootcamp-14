import json
from pprint import pprint
from urllib.request import urlopen


response = urlopen("http://services.groupkt.com/country/get/all")
countries = response.read()

pprint (countries)
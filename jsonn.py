import json
import requests

r = requests.get(url="https://www.cryptocompare.com/api/data/coinlist/")
dat = r.json()

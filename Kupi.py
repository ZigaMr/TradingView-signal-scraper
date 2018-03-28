from Crypto_signals import Browse_Signals
import requests,json


a = Browse_Signals()

for i in a[0]:
    if i == ["bitcoin","dollar"]:
        resp = requests.get(url="https://www.bitstamp.net/api/v2/ticker/btcusd/").json()
        print(resp)
import requests

def get_bitstamp_ticker():
    req = requests.get('https://www.bitstamp.net/api/ticker/')
    return req.json()

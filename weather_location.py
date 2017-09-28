from flask import jsonify
import urllib.request
import time
def get_coordonates():
        r = urllib.request.urlopen("http://ip-api.com/json").read()
        return r

def get_weather(lat=0,lon=0):
    key = "7cb9a1ff7df8d773b4f09cf5e7c3692d"
    r = urllib.request.urlopen("https://api.darksky.net/forecast/{}/{},{}".format(key,lat,lon)).read()
    return r

def get_icon(text):
    return "Hello {}".format(text);

def get_date(timestamp):
    x = time.localtime(timestamp)
    return "{}/{}/{} {}H{}min".format(x.tm_mon, x.tm_mday, x.tm_year, x.tm_hour, x.tm_min)

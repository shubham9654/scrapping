import requests, time, json
from bs4 import BeautifulSoup
from pprint import pprint

base_url = "https://www.buzzfeed.com/in"
reqUrl = requests.get(base_url)
reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')

featured_article = reqSoup.find("article", "card featured-card xs-relative xs-mb05 md-mb1 xs-border-left-none xs-border-right-none md-border-lighter js-feed-item js-feed-item--filtered")
pprint(featured_article)

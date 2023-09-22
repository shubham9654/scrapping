import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://shishjewels.com/2022/01/08/custom-hip-hop-jewelry/"
reqUrl = requests.get(url)
reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')

blog_data = {}
blog_title = reqSoup.find('h1', 'page-title').get_text()
blog_date = reqSoup.find('li', 'item-date').get_text()
blog_content = reqSoup.find('div', 'entry-content clearfix')

blog_data["blog_title"] = blog_title
blog_data["blog_date"] = blog_date
blog_data["blog_content"] = str(blog_content)

print(blog_data, 'dfffffffffffffff')

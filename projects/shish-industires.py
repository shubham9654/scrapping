import requests,json,pprint,os,time,random
from bs4 import BeautifulSoup

url= requests.get("https://shishindustries.com/investors/corporate-announcement/")
parsedUrl=BeautifulSoup(url.text,'html.parser')
mainDiv= parsedUrl.find('div',class_='et_pb_section et_pb_section_2 et_section_regular')
rowCards = mainDiv.findAll('div', class_='et_pb_row')

allRequiredATags = []

yearCount = -1
for cards in rowCards:
  mainCards = cards.findAll('div', class_='et_pb_column')
  for card in mainCards:
    yearCount = yearCount + 1
    yearTitle = card.find('h3').get_text()
    pTag = card.find('p')
    allRequiredATags.append({
      "label": yearTitle,
      "value": []
    })
    if pTag:
      allATags = pTag.findAll('a')
      for aTag in allATags:
        aText = aTag.get_text()
        aHref = aTag['href']
        allRequiredATags[yearCount]["value"].append({
          "title": aText,
          "link": aHref
        })

print(allRequiredATags)



import requests, time, json
from bs4 import BeautifulSoup
from pprint import pprint

base_url = "https://pagalworldi.com"
main_url = "https://pagalworldi.com/list/bollywood-movies-mp3-songs-2022s/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def getSongDescription(url):
  reqUrl = requests.get(url, headers=headers)
  reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')
  req_song_url = reqSoup.find('source').get('src')
  song_download_url = base_url + req_song_url
  return song_download_url

def getSongs(url):
  count = 1
  song_list = []
  reqUrl = requests.get(url, headers=headers)
  reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')
  time.sleep(2)
  main_div = reqSoup.find('ul', 'list')
  all_songs = main_div.find_all('li')

  for song in all_songs:
    song_detail = {
      "song_title": "",
      "song_desc": "",
      "song_img_url": "",
      "song_download_url": ""
    }

    song_title_el = song.find('h3')
    if song_title_el != None:
      song_detail["song_title"] = song_title_el.get_text()

    song_desc_el = song.find('p')
    if song_desc_el != None:
      song_detail["song_desc"] = song_desc_el.get_text()
    
    song_img_el = song.find('img')
    if song_img_el != None:
      song_detail["song_img_url"] = song_img_el.get('src')

    song_url = song.find('a')
    if song_url != None:
      req_song_url = song_url.get('href')
      req_url = base_url + req_song_url
      song_download_url = getSongDescription(req_url)
      song_detail["song_download_url"] = song_download_url

    song_list.append(song_detail)

    print(f"song_no=${count}")
    count += 1
    time.sleep(1)
    break
  
  return song_list

main_song_list = []
for page in range(2):
  print(f"\n========================== page_no={page+1} ========================\n")
  hit_url = main_url + str(page + 1) + ".html"
  song_list = getSongs(hit_url)
  main_song_list.extend(song_list)

  time.sleep(1)
  break

file_name = "bollywood_2022_year_songs.json"
with open(file_name, 'w') as file:
  json.dump(main_song_list, file, indent=2)


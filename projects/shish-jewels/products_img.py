import time, os, requests, threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

browser = webdriver.Chrome()
url = "http://shishjewels.com/product-category/pendants/"
time.sleep(2)

def downloadProductImg(img_url):
  url = img_url
  filename = os.path.basename(url)

  response = requests.get(img_url)
  image_data = response.content
  directory_name = "pendants/"
  directory_path = "/home/shubhamsarkar/Desktop/bruce/python-project/scrapping/images/" + directory_name
  os.makedirs(directory_path, exist_ok=True)
  local_image_path = os.path.join(directory_path, f"{filename}")

  with open(local_image_path, "wb") as image_file:
    image_file.write(image_data)

def getProductDetail(url):
  reqUrl = requests.get(url)
  reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')
  main_div = reqSoup.find('div', 'woocommerce-product-gallery__image')

  main_img = main_div.find('img', 'wp-post-image').get('src')
  zoom_img = main_div.find('a').get('href')
  downloadProductImg(main_img)
  downloadProductImg(zoom_img)

def getProductList(url):
  browser.get(url)
  product_list_ui = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/main/ul")  # get all product list
  all_products = product_list_ui.find_elements(By.XPATH, ".//li")

  count = 1
  threads = []
  for product in all_products:
    product_url = product.find_element(By.XPATH, ".//a").get_attribute("href")

    product_container = product.find_element(By.CLASS_NAME, "woocommerce-product-inner")
    product_img_url = product_container.find_element(By.XPATH, './/img[@class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail"]').get_attribute("src")
    # product_name = product_container.find_element(By.XPATH, './/h3[@class="woocommerce-product-title"]/a').text.lower().replace(" ", "_")

    downloadProductImg(product_img_url)
    getProductDetail(product_url)
    thread = threading.Thread(target=getProductDetail, args=(product_url,))
    threads.append(thread)
    thread.start()

    print(count)
    count += 1

  for thread in threads:
    thread.join()

def fetchByPages(): # function used to fetch data by number of pages
  browser.get(url)
  ui_page_list = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/main/nav/ul")
  all_page_list = ui_page_list.find_elements(By.XPATH, ".//li")

  for page in range(len(all_page_list) - 1):
    if page == 0:
      getProductList(url)
    else:
      new_url = url + "/page/" + str(page + 1)
      getProductList(new_url)

fetchByPages()
browser.quit()

import time, os, json, requests, threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

browser = webdriver.Chrome()
browser.get("http://shishjewels.com/product-category/watches/")
time.sleep(1)

def getProductDetail(url):
  product_description = {}
  reqUrl = requests.get(url)
  reqSoup = BeautifulSoup(reqUrl.content, 'html.parser')
  main_div = reqSoup.find('div', 'woocommerce-summary-wrap row')

  product_detail_img = main_div.find('img').get('src')
  product_detail = main_div.find('div', 'col-xl-6 col-lg-6 col-md-6')
  product_short_description = product_detail.find('div', 'woocommerce-product-details__short-description')
  product_meta = product_detail.find('div', 'product_meta')
  
  product_description["product_detail_img"] = product_detail_img
  product_description["product_short_description"] = product_short_description
  product_description["product_meta"] = product_meta
  return product_description

def getProductList():
  product_list_ui = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/main/ul")  # get all product list
  all_products = product_list_ui.find_elements(By.XPATH, ".//li")

  count = 1
  reqProductList = {"category": "Watches", "products": []}
  for product in all_products:
    product_url = product.find_element(By.XPATH, ".//a").get_attribute("href")
    product_description = getProductDetail(product_url)
    product_container = product.find_element(By.CLASS_NAME, "woocommerce-product-inner")
    product_img = product_container.find_element(By.XPATH, './/img[@class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail"]').get_attribute("src")
    product_h3_text = product_container.find_element(By.XPATH, './/h3[@class="woocommerce-product-title"]/a').text

    reqProductList["products"].append({
      "product_url": product_url,
      "product_img": product_img,
      "product_title": product_h3_text,
      "product_description": product_description
    })
    print(count)
    count += 1
  return reqProductList

product_list = getProductList()
print(product_list)
browser.quit()

# filename = "data.json"
# if os.path.exists(filename):
#   with open(filename, 'r') as file:
#     existing_data = json.load(file)
#     existing_data.update(reqProductList)
#     with open(filename, 'w') as file:
#         json.dump(existing_data, file, indent=4)
# else:
#   with open(filename, 'w') as file:
#     json.dump(reqProductList, file, indent=4)

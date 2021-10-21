# %%

import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from uuid import uuid4


firefox = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

url = "https://www.asos.com/men/a-to-z-of-brands/gramicci/cat/?cid=29936"

firefox.get(url)

product_tags = firefox.find_elements(By.XPATH, '//a[@class="_3TqU78D"]')
# print(product_tags)


def get_product_information(product_tag):

    product = {}

    product_name = product_tag.find_element(By.XPATH, './div/div/div/h2')
    product["name"] = product_name.text

    price = product_tag.find_element(By.XPATH, './p/span/span')
    product["price"] = price.text

    product_img = product_tag.find_element(By.XPATH, './/img')
    src = product_img.get_attribute('src')
    img_name = product["name"].title().replace(' ', '_').strip('Gramicci_')
    product["img_name"] = img_name
    
    brand_name = product["name"].split()[0]
    directory_maker(f'images/{brand_name}/{img_name}')
    img_downloader(src, f'images/{brand_name}/{img_name}/{uuid4()}.jpg')

    print(product)


def directory_maker(path):

    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path)


def img_downloader(url, path):

    if url == None:
        pass
    else:
        img_data = requests.get(url).content
        with open(path, 'wb') as handler:
                    handler.write(img_data)


for product_tag in product_tags:
    #print(product_tag)
    get_product_information(product_tag)


# %% Class

class AsosScraper:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def scrape(self):
        self.driver.get(self.url)
        self.product_tags = self.driver.find_elements(By.XPATH, '//a[@class="_3TqU78D"]')
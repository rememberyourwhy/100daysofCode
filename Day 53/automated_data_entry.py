# import selenium
import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bs4 import BeautifulSoup
import requests
from lxml import etree


GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/" \
                   "1FAIpQLSeF-BUJdwHyZ6bnget-r0p7hZIdZvyb4GMqgd5HX2f2Uiw6SQ" \
                   "/viewform?usp=sf_link"

# https://docs.google.com/forms/d/e/1FAIpQLSeF-BUJdwHyZ6bnget-r0p7hZIdZvyb4GMqgd5HX2f2Uiw6SQ/viewform?usp=sf_link

ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/" \
              "?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
              "mapBounds%22%3A%7B%22west%22%3A-" \
              "122.83501662207031%2C%22east%22%3A-" \
              "122.03164137792969%2C%22south%22%3A37." \
              "545901564546206%2C%22north%22%3A38." \
              "003971804876244%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22" \
              "filterState%22%3A%7B%22price%22%3A%7B%22" \
              "max%22%3A872627%7D%2C%22beds%22%3A%7B%22" \
              "min%22%3A1%7D%2C%22fore%22%3A%7B%22" \
              "value%22%3Afalse%7D%2C%22mp%22%3A%7B%22" \
              "max%22%3A3000%7D%2C%22auc%22%3A%7B%22" \
              "value%22%3Afalse%7D%2C%22nc%22%3A%7B%22" \
              "value%22%3Afalse%7D%2C%22fr%22%3A%7B%22" \
              "value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22" \
              "value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22" \
              "value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22" \
              "value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

ACCEPT_LANGUAGE = "vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"

headers = {
    "accept-language": ACCEPT_LANGUAGE,
    "user-agent": USER_AGENT,
}


# class ZillowScraping:  # by Selenium
#     # FAILED
#     def __init__(self):
#         s = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=s)
#         self.driver.get(ZILLOW_LINK)
#
#         # response = requests.get(url=ZILLOW_LINK, headers=headers)
#         # contents = response.text
#         #
#         # self.soup = BeautifulSoup(contents, "html.parser")
#
#         self.list_tags = []
#
#         run = False
#
#         while not run:
#             run = input("RUN? ")
#
#         self.get_all_info()
#
#     def get_all_info(self):
#         self.list_tags = self.driver.find_elements(
#             By.CSS_SELECTOR,
#             ".grid-search-results li"
#         )
#
#     @staticmethod
#     def get_address(list_tag):
#         address_tag = list_tag.find_element(By.CSS_SELECTOR, "address")
#         print(address_tag.text)
#         return address_tag.text
#
#     @staticmethod
#     def get_price(list_tag):
#         price_tag = list_tag.find_element(By.XPATH, "//span[@data_test='property-card-price']")
#         print(price_tag.text)
#         return price_tag.text
#
#     @staticmethod
#     def get_link(list_tag):
#         a_tag = list_tag.find_element(By.CSS_SELECTOR, "a")
#         print(a_tag.get_attribute("href"))
#         return a_tag.get_attribute("href")

class ZillowScraping:  # by Selenium
    # FAILED
    def __init__(self):
        response = requests.get(url=ZILLOW_LINK, headers=headers)
        contents = response.text

        self.soup = BeautifulSoup(contents, "html.parser")

        self.list_tags = []

        self.get_all_info()

    def get_all_info(self):
        ul_tag = self.soup.select_one(selector="#search-page-list-container div ul")
        self.list_tags = ul_tag.find_all(name="li")

    @staticmethod
    def get_address(list_tag):
        address_tag = list_tag.select_one("address")
        print("ADDRESS:")
        print(address_tag.text)

        return address_tag.text

    @staticmethod
    def get_price(list_tag):

        price_tag = list_tag.find(name="span")

        print("PRICE: ")
        print(price_tag.getText())
        return price_tag.getText()

    @staticmethod
    def get_link(list_tag):
        soup_list_tag = BeautifulSoup(str(list_tag), "html.parser")
        a_tag = soup_list_tag.select_one("a")

        print("LINK: ")
        print(a_tag["href"])
        return str(a_tag["href"])


class FormBot:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(GOOGLE_FORM_LINK)

        self.address_input = None
        self.price_input = None
        self.link_input = None
        self.submit_btn = None

        self.detect_input_fields()

    def detect_input_fields(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                "//div[@role='list']")))
        outer_div_tag = self.driver.find_element(By.XPATH, "//div[@role='list']")
        inputs = WebDriverWait(outer_div_tag, 20).until(
            EC.presence_of_all_elements_located((
                By.CSS_SELECTOR,
                "input")))

        self.address_input = inputs[0]
        self.price_input = inputs[1]
        self.link_input = inputs[2]

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[@role='button']")))
        self.submit_btn = self.driver.find_element(By.XPATH, "//div[@role='button']")

    def send_keys_to_address_price_link(self, address_val, price_val, link_val):
        try:
            self.address_input.send_keys(address_val)
            self.price_input.send_keys(price_val)
            self.link_input.send_keys(link_val)
            self.submit_btn.click()
        except:
            return 1
        return 0
        
        
zc = ZillowScraping()
for li in zc.list_tags:
    print(li)
    try:
        address = zc.get_address(li)
        price = zc.get_price(li)
        link = zc.get_link(li)
    except AttributeError:
        continue
    else:
        form_bot = FormBot()
        form_bot.detect_input_fields()
        form_bot.send_keys_to_address_price_link(address, price, link)

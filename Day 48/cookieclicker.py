from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = r"https://orteil.dashnet.org/cookieclicker/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)


def language_select():
    try:
        english_button = driver.find_element(by=By.CLASS_NAME, value="langSelectButton")
    except:
        pass
    else:
        english_button.click()
        time.sleep(10)


def click_cookie():
    cookie_button = driver.find_element(by=By.ID, value="bigCookie")
    cookie_button.click()


def click_building():
    try:
        building_buttons = driver.find_elements(by=By.CLASS_NAME, value="enabled")
        building_button_highest = building_buttons[-1]
        building_button_highest.click()
    except:
        pass


time.sleep(20)

language_select()


time_out = time.time() + 5


while True:
    click_cookie()
    if time.time() > time_out:
        click_building()
        time_out = time.time() + 5






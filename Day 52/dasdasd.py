from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# ------------ CONSTANTS ------------- #

INS_EMAIL = "youremail@gmail.com"
INS_PASSWORD = "yourpassword"
INS_URL = "https://instagram.com"


class InstaFollower:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(INS_URL)

        time.sleep(3)

        username_input_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input_tag.send_keys(INS_EMAIL)

        password_input_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input_tag.send_keys(INS_PASSWORD)
        password_input_tag.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(2)

        self.driver.get("https://www.instagram.com/geeks_for_geeks/")
        # change the link above to your instagram link

        time.sleep(3)

        followers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.PARTIAL_LINK_TEXT,
                'followers')))
        # The line above is optional, you can change followers to following
        followers.click()

        time.sleep(3)

        try:
            popup = self.driver.find_element(
                    By.CSS_SELECTOR,
                    '._aano')
        except:
            print("FAILED TO FIND POPUP ELEMENT")

        else:
            print("Popup element is found")

        for run in range(100):
            print(f"scrolling down {run}")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)


insta_follower_bot = InstaFollower()
insta_follower_bot.login()
time.sleep(2)
insta_follower_bot.find_followers()

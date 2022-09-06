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

INS_EMAIL = os.getenv("INS_EMAIL")
INS_PASSWORD = os.getenv("INS_PASSWORD")
INS_URL = "https://instagram.com"


class InstaFollower:
    def __init__(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get(INS_URL)

        username_input_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username_input_tag.send_keys(INS_EMAIL)

        password_input_tag = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        password_input_tag.send_keys(INS_PASSWORD)
        password_input_tag.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(2)

        self.driver.get("https://www.instagram.com/geeks_for_geeks/followers/")

        time.sleep(3)

        # Scroll till Followers list is there


    def follow(self):
        time.sleep(5)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in all_buttons:
            try:
                action = ActionChains(self.driver)
                action.move_to_element(button).perform()
                time.sleep(1)
                button.click()
                print("clicking")
                time.sleep(1)
            except:
                print("EXCEPTION OCCURRED")
                cancel_button = self.driver.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
                )
                cancel_button.click()


insta_follower_bot = InstaFollower()
insta_follower_bot.login()
time.sleep(2)
insta_follower_bot.find_followers()
insta_follower_bot.follow()

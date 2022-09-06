from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# ------------ CONSTANTS ------------- #
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PHONE_NUMBER = os.getenv("TWITTER_PHONE_NUMBER")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

URL = r"https://twitter.com/i/flow/login"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)


def twitter_auto_login():

        time.sleep(10)

        username_input = driver.find_element(By.CSS_SELECTOR, "input")
        username_input.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        username_input.send_keys(Keys.ENTER)

        time.sleep(5)

        phone_num_input = driver.find_element(By.CSS_SELECTOR, "input")
        phone_num_input.send_keys(TWITTER_PHONE_NUMBER)
        time.sleep(2)
        phone_num_input.send_keys(Keys.ENTER)

        time.sleep(5)

        password_input = driver.find_element(By.CSS_SELECTOR, "input")
        # driver.execute_script("arguments[0].click();", password_input)
        driver.execute_script("arguments[0].value=arguments[1];", password_input, TWITTER_PASSWORD)
        # https://stackoverflow.com/questions/52273298/what-is-arguments0-while-invoking-execute-script-method-through-webdriver-in

        time.sleep(2)

        driver.execute_script("var script = document.createElement('script'); script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; var e = $.Event( 'keypress', { which: 13 } );arguments[0].trigger(e);", password_input)

# def twitter_auto_login():
#     username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='username']")))
#     username_input.send_keys(TWITTER_EMAIL)
#     username_input.send_keys(Keys.ENTER)
#
#     phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='on']")))
#     phone_input.send_keys(TWITTER_PHONE_NUMBER)
#     phone_input.send_keys(Keys.ENTER)
#
#     password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']")))
#     password_input.send_keys(TWITTER_PASSWORD)
#     password_input.send_keys(Keys.ENTER)
#
#
# twitter_auto_login()


def twitter_post_complaint(up_speed, down_speed):

    draft_input_tag = driver.find_element(By.CSS_SELECTOR, "public-DraftStyleDefault-block")
    complaint_msg = f"""
Hey @Comcast why is my internet speed {down_speed}down\\{up_speed}up when I pay for 150down\\10up in Washington DC?
@ComcastCares @xfinity #comcast #speedtest
    """
    draft_input_tag.send_keys(complaint_msg)

    time.sleep(1)

    tweet_btn_css_selector = "div[data-testid='tweetButtonInline']"
    tweet_btn = driver.find_element(By.CSS_SELECTOR, tweet_btn_css_selector)
    tweet_btn.click()


print("STARTING TO LOG IN")
twitter_auto_login()
time.sleep(5)
print("STARTING TO POST COMPLAIN")
twitter_post_complaint("10", "10")
time.sleep(5)

driver.quit()


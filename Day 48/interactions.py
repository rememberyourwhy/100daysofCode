from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = r"http://secure-retreat-92358.herokuapp.com/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)

# articles_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(articles_count.text)

# button = driver.find_element(by=By.LINK_TEXT, value="Button0")
# new_url = button.get_attribute("href")
# print(new_url)
# driver.get(url=new_url)
#
# while True:
#     pass

f_name = driver.find_element(by=By.NAME, value="fName")
f_name.send_keys("ABCDEF")
l_name = driver.find_element(by=By.NAME, value="lName")
l_name.send_keys("ABCDEF")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("phuc16052001@gmail.com")
sign_up_button = driver.find_element(by=By.CLASS_NAME, value="btn")
sign_up_button.click()

while True:
    pass



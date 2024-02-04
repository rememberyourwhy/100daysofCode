from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import lxml
import pickle

options = webdriver.ChromeOptions()
s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)

driver.get("https://www.google.com/")
input("WAIT")
driver.close()
input("WAIT")
driver.get("https://www.google.com/")
input("WAIT")
driver.get("https://www.google.com/")
input("WAIT")
driver.quit()
input("QUITED")
driver.get("https://www.google.com/")

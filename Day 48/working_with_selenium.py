# pip3 install -U selenium
# pip3 install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
URL = r"https://www.python.org/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)

# DOCUMENTATION LINK: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
price = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(price.get_property("href"))

# driver.close() # close 1 tab
# driver.quit() # close the browser

# A VERY USEFUL USE OF FIND_ELEMENT
# By.CSS_SELECTOR

# <div class="small-widget documentation-widget">
#   <h2 class="widget-title"><span aria-hidden="true" class="icon-documentation"></span>Docs</h2>
#   <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
#   <p><a href="https://www.python.org/">docs.python.org</a></p>
# </div>

# Let say we want to get the documentation link, which is https://www.python.org/

# CODE:
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# Important method of selenium class:
# get_property
#     sample code:
#     from selenium import webdriver
#     from selenium.webdriver.chrome.service import Service
#     from webdriver_manager.chrome import ChromeDriverManager
#     from selenium.webdriver.common.by import By
#     import time
#     URL = r"https://www.python.org/"
#
#     s = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=s)
#
#     driver.get(url=URL)
#
#     # DOCUMENTATION LINK: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
#     price = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
#     print(price.get_property("href"))
#     or get_attribute
#     I should learn about these

# size
# get_attribute
#     sample code:
#     print(price.get_attribute("placeholder"))

# SEARCH ELEMENTS USING XPATH:
# JUST GO TO THAT ELEMENT CODE IN DEVELOPER MENU: CTRL SHIFT I
# RIGHT MOUSE, SELECT COPY -> COPY XPATH

driver.quit()

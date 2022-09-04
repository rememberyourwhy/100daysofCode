from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = r"https://www.python.org/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)

upcoming_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

date_list = []
event_list = []

for upcoming_event in upcoming_events:
    time_tag = upcoming_event.find_element(By.CSS_SELECTOR, value="time")
    date = time_tag.get_attribute("datetime").split("T")[0]
    date_list.append(date)
    a_tag = upcoming_event.find_element(By.CSS_SELECTOR, value="a")
    event_name = a_tag.text
    event_list.append(event_name)

event_dictionary = {
    index: {
        "time": date,
        "name": event_name,
    } for index, date, event_name in zip(range(0, len(upcoming_events)), date_list, event_list)
}

print(event_dictionary)


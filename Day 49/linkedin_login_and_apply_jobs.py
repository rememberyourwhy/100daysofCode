from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = r"https://www.linkedin.com/"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url=URL)

# DOCUMENTATION LINK: https://selenium-python.readthedocs.io/locating-elements.html#locating-elements


# ACTION FUNCTIONS
# CLICK NEXT BUTTON
def click_next_button():
    next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    next_button.click()

# ------------------------- SIGN IN LINKEDIN ------------------- #
def sign_in():
    signin_btn = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
    signin_btn.click()
    time.sleep(10)
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("phuc160520011@gmail.com")
    password_input.send_keys("Pt17122003")
    signin_btn_2 = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large")
    signin_btn_2.click()
    time.sleep(10)


# --------------------------- ENTER JOB SECTION ----------------- #
def enter_job_section():
    job_btn = driver.find_elements(By.CSS_SELECTOR, ".global-nav__nav li")[2]
    job_btn.click()
    time.sleep(5)


# --------------------------- SENDKEYS TO SEARCH MENU ------------ #
def search_for_job():
    search_job_input = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
    search_job_input.send_keys("python developer")
    time.sleep(3)
    search_location_input = None
    search_location_input = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__input--location input")

    # for element in search_location_input_prob:
    #     try:
    #         element_aria_label = element.get_attribute("aria-label")
    #     except:
    #         continue
    #     else:
    #         if element_aria_label == "City, state, or zip code":
    #             search_location_input = element
    #             print(search_location_input.text)
    if search_location_input is None:
        print("FAILED TO DETECT LOCATION SEARCH BAR")
        exit()
    search_location_input.send_keys("Remote")
    time.sleep(1)
    search_location_input.send_keys(Keys.ENTER)
    time.sleep(5)
    easy_apply_filters_btn = driver.find_element(By.CSS_SELECTOR, ".search-reusables__filter-binary-toggle")
    easy_apply_filters_btn.click()
    time.sleep(1)


def apply_for_a_job():
    jobs_result_btn = driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__list-container li a")
    jobs_result_btn.click()
    time.sleep(2)
    easy_apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
    easy_apply_btn.click()
    time.sleep(1)
    mobile_phone_number_input = driver.find_element(By.CSS_SELECTOR, ".ember-text-field")
    # IF THE FIELD IS FILLED, DELETE BEFORE TYPE IN MY PHONE NUMBER
    mobile_phone_number_input.send_keys(Keys.CONTROL+"A")
    mobile_phone_number_input.send_keys(Keys.DELETE)
    mobile_phone_number_input.send_keys("0379809157")
    time.sleep(1)
    click_next_button()
    # next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    # next_button.click()
    time.sleep(2)

    # ENTER THE RESUME SESSION
    click_next_button()
    # next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    # next_button.click()
    time.sleep(2)

    # ENTER THE ADDITIONAL QUESTIONS SESSION
    #   ASK IF I FINISHED BACHELOR's DEGREE:
    yes_no_buttons = driver.find_elements(By.CSS_SELECTOR, ".fb-radio label")
    no_button = yes_no_buttons[1]
    no_button.click()
    #   ASK MY LEVEL IN ENGLISH
    select_dropdown = driver.find_element(By.CSS_SELECTOR, ".fb-dropdown select")
    select_dropdown.click()
    #   SELECT CONVERSATIONAL
    select_conversational = select_dropdown.find_elements(By.CSS_SELECTOR, "option")[2]
    select_conversational.click()
    #   CLICK REVIEW BUTTON
    click_next_button()
    # review_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    # review_button.click()
    time.sleep(2)
    #   SUBMIT APPLICATION
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    click_next_button()
    # submit_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
    # submit_button.click()
    time.sleep(2)


time.sleep(5)
print("STARTING TO SIGN IN")
sign_in()
print("STARTING TO ENTER JOB SECTION")
enter_job_section()
print("STARTING TO SEARCH FOR JOB")
search_for_job()
print("STARTING TO APPLY THE FIRST JOB")
apply_for_a_job()
print("EASYYYYYYYYYYYYYYYYYYYYY")

"""    
HOW TO UPGRADE:

MAKE A FUNCTION TO DETECT THE STATE OF APPLYING:

    THIS FUNCTION WILL RETURN ONE OF THESE VALUES:
        +NOT ENTERED JOB APPLYING
        +ESSENTIAL INFORMATION
        +RESUME
        +ADDITIONAL QUESTIONS
        +REVIEW
        +PROCESS FINISHED

    HAVE A FUNCTION TO FINISH EACH STATE
        
"""

while True:
    time.sleep(10)



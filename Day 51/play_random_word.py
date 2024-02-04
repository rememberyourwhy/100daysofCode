from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ------------ CONSTANTS ------------- #

LESSON_URL = "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/"
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
FIRST_WORD = "uncle"
LAST_WORD = "rain"


def get_a_button(all_buttons):
    import random
    a = random.choice(all_buttons)
    print(all_buttons.index(a))
    return a


def play_buttons():
    def slow_mode():
        # Turn off AD
        # try:
        #     ad_close_button= WebDriverWait(driver, 10).until(
        #                         EC.presence_of_element_located((
        #                             By.XPATH, "//a[@class='ancr-close']")))
        #     ad_close_button.click()
        # except:
        #     print("Need to close the ad manually")

        while input("STOP?") != "STOP":
            random_button = get_a_button(filtered_all_buttons)

            driver.execute_script('arguments[0].scrollIntoView();', random_button)
            random_button.send_keys(Keys.DOWN)
            try:
                random_button.click()
            except:
                pass
            if input("Need hint? ") == "Y":
                translation = random_button.find_element(By.XPATH, "..//span").get_attribute("title")
                print(translation)

    def none_stop_mode():
        pass

    driver.get(LESSON_URL)
    first_word, last_word = FIRST_WORD, LAST_WORD
    first_word_index, last_word_index = None, None
    all_buttons = driver.find_elements(By.XPATH, "//div[@class='entry-content']/p/button")
    print(len(all_buttons))
    print(all_buttons)
    # Find first/last button
    for i in range(len(all_buttons)):
        print(i)
        # Check if the name attribute of span tag is first_word/ last_word.
        try:
            span_tag_name = all_buttons[i].find_element(By.XPATH, "../span").get_attribute("title")
        except:
            span_tag_name = all_buttons[i].find_element(By.XPATH, "../a/following-sibling::br")
            print("SPAN_TAG_NAME VALUE ERROR")
        if span_tag_name == first_word:
            first_word_index = i
        if span_tag_name == last_word:
            last_word_index = i
            break
    if (first_word_index or last_word_index) is None:
        print("Invalid first_word / last_word")
        return
    filtered_all_buttons = all_buttons[first_word_index: last_word_index + 1]
    slow_mode()


play_buttons()

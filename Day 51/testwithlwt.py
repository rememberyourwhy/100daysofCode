
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


# ------------ CONSTANTS ------------- #

LESSON_URL = "http://127.0.0.1/lwt/index.php"
HTML_DOC = r"C:\Users\Hii\Downloads\Python Files\LingQ pages\Who_is_she\English\LingQ Learning Languages Simply.html"

# ------ Setup selenium with normal cookie --- #
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Hii\AppData\Local\Google\Chrome\User Data")
options.add_argument('--no-sandbox')
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-extensions")

# ----- Setup selenium for download ---- #
# Document link: https://www.browserstack.com/guide/download-file-using-selenium-python
SERIES_NAME = "TEXT"
TEXT_PATH = r"C:\Users\Hii\Downloads\lwt\To_import\English\LingQ\A1\Who_is_she\Text"
DOWNLOAD_PATH = r"C:\Users\Hii\Downloads\lwt\To_import\English\LingQ\A1\Who_is_she\Audio"
prefs = {"download.default_directory": DOWNLOAD_PATH}
options.add_experimental_option("prefs", prefs)

s = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)


def turn_off_streak_notif(_driver):
    try:
        streak_notif = WebDriverWait(_driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        streak_notif_off_button = streak_notif.find_element(By.TAG_NAME, "button")
        streak_notif_off_button.click()
    except:
        pass


def back_to_the_start_of_the_lesson(_driver):
    # nav = navigation bar
    not_at_the_start = True
    while not_at_the_start:
        try:
            left_nav = WebDriverWait(_driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "nav--left"))
            )
            left_nav_button = left_nav.find_element(By.XPATH, "./a[@role='button']")
            left_nav_button.click()
        except:
            not_at_the_start = False


def extract_stories_links():
    with open(HTML_DOC, 'r', encoding='utf-8', errors='ignore') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
    link_list = []
    for link in soup.select('.is-extended'):
        link_list.append(link['href'])
    return link_list


def extract_mp3_link(_driver):
    mp3_link = None
    a_tag_list = WebDriverWait(_driver, 5).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )
    for tag in a_tag_list:
        href_string = str(tag.get_attribute("href"))
        if "mp3" in href_string:
            mp3_link = tag.get_attribute("href")
            break
        print(mp3_link)
    return mp3_link


def download_mp3_file(_link):
    driver.get(_link)


def extract_text(story_link):
    driver.get(story_link)

    turn_off_streak_notif(driver)
    back_to_the_start_of_the_lesson(driver)

    text = ""
    still_next_page = True
    while still_next_page:
        sentence_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "sentence"))
        )
        for sentence in sentence_list:
            if len(sentence.text) == 0:
                continue
            sentence_text = ""
            sentence_item_span_tag = sentence.find_elements(By.XPATH, "./span")
            for count, tag in enumerate(sentence_item_span_tag, start=1):
                sentence_text += tag.text

                # add white space or end sentence symbol
                if count != len(sentence_item_span_tag):
                    sentence_text += " "
                else:
                    try:
                        sentence_text += sentence.text[-1]
                    except:
                        pass
                print(tag.text)

            text += sentence_text
            text += "\n"

        try:
            next_page_button = driver.find_element(By.CLASS_NAME, "next-page-button")
            next_page_button.click()
            try:
                i_know_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'I know these words')]"))
                )
                i_know_button.click()
            except:
                pass
        except:
            still_next_page = False

    return text


def main():
    driver.get("https://www.google.com/")
    driver.execute_script("window.open('about:blank','secondtab')")
    driver.switch_to.window("secondtab")
    # link_list = extract_stories_links()
    link_list = [
        "https://www.lingq.com/en/learn/en/web/reader/20286"
    ]
    for count, link in enumerate(link_list, start=1):
        result_text = extract_text(link)
        mp3_link = extract_mp3_link(driver)
        download_mp3_file(mp3_link)

        # save the text to txt file
        file_name = f"{SERIES_NAME}_{count}.txt"
        file_path = f"{TEXT_PATH}\\{file_name}"
        with open(file_path, 'wb') as result_file:
            result_file.write(bytes(result_text, 'utf-8'))
        print(f"FILE {count}.txt is saved")
        # if input("CONTINUE? ") == "STOP":
        #     driver.quit()
    driver.quit()


input("WAIT")

main()

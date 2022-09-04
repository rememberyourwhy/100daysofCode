import requests
from bs4 import BeautifulSoup
from send_email import send_mail

# BeautifulSoup Uses:
# Sample Code:

# response = requests.get(billboard_link_with_date)
# contents = response.text
#
# soup = BeautifulSoup(contents, "html.parser")

URL = "https://www.amazon.com/dp/B0B497HTJ8/ref=sbl_dpx_kitchen-electric-cookware_B0B96KNQ7T_0"
ACCEPT_LANGUAGE = "vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"
TARGET_PRICE = 120.0

headers = {
    "accept-language": ACCEPT_LANGUAGE,
    "user-agent": USER_AGENT,
}

response = requests.get(url=URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")


# price_tag = soup.select()
# print(price_tag.getText())
product_name = soup.find(name="title").text


price_tag = soup.find(name="span", class_="a-offscreen")
price_text = price_tag.text.split("$")[1]

price = float(price_text)
print(price)
print(price < TARGET_PRICE)

if price < TARGET_PRICE:
    mail_subject = "Amazon Price Alert"
    mail_content = f"{product_name} is now {price}"
    send_mail(mail_subject, mail_content)


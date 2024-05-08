import re
from bs4 import BeautifulSoup
# open text file & read
import regex


def is_hangul(value):
    if regex.search(r'\p{IsHangul}', value):
        return True
    return False


with open("./Input/Sentence Mining__Clozemaster.txt", mode="r", encoding='utf-8') as t_input_file:
    text_string = t_input_file.read()
soup = BeautifulSoup(text_string, 'html.parser')
u_list = soup.find_all('u')

hangul_list = []
for u_element in u_list:
    hangul_list.append(u_element.text)
span_list = soup.find_all('span')
for span_element in span_list:
    span_text = span_element.text
    if is_hangul(span_text):
        hangul_list.append(span_text)

hangul_string = " ".join(hangul_list)
path = f"./Output/1.txt"
with open(path, mode="w", encoding='utf-8') as finished_output:
    finished_output.write(hangul_string)

import re
import glob, os


OBJECT_NAME = "strong_girl"
def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None

def get_word(s):
    l_in_bracket = re.findall("(?<=\[).+?(?=\])", s)
    if l_in_bracket:
        return l_in_bracket[0]


os.chdir("input/input2/")
txt_files = glob.glob("*.txt")

dict_word_count = {}

# for d_file in txt_files:
#     with open(d_file, mode="r", encoding="utf-8") as input_file:
#         file_str = input_file.read()
#         word_count_list = file_str.split("\n")
#     result = ""
#     for line in word_count_list:
#         word_count = get_trailing_number(line)
#         if word_count and (word_count > 5):
#             result += line
#             result += "\n"

for d_file in txt_files:
    with open(d_file, mode="r", encoding="utf-8") as input_file:
        file_str = input_file.read()
        word_count_list = file_str.split("\n")
    for line in word_count_list:
        word_count = get_trailing_number(line)
        word = get_word(line)
        if word_count:
            if dict_word_count.get(word):
                dict_word_count[word] += word_count
            else:
                dict_word_count[word] = word_count

result = ""
for key, value in dict_word_count.items():
    if value > 5:
      result += f"{key} {value}"
      result += "\n"
os.chdir("../../")
path = f"output/{OBJECT_NAME}.txt"
with open(path, mode="w", encoding="utf-8") as finished_output:
    finished_output.write(result)
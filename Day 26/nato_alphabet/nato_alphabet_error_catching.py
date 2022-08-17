import pandas

# ----------------------------- Approach 1: use while loop ----------- #
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# letter_code = {row.letter.lower(): row.code for index, row in data.iterrows()}
#
# run = True
# while run:
#     name = input("Type your name: ")
#     try:
#         code_list = [letter_code[letter.lower()] for letter in name]
#     except KeyError("No number please"):
#         run = True
#     else:
#         run = False
#         print(code_list)

# ---------------- Approach 2: create function and use recursion -------- #
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code = {row.letter.lower(): row.code for index, row in data.iterrows()}


def generate_phonetic():
    name = input("Type your name: ")
    try:
        code_list = [letter_code[letter.lower()] for letter in name]
    except KeyError:
        generate_phonetic()
    else:
        print(code_list)

generate_phonetic()
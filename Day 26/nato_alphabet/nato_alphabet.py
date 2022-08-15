# read csv file
# convert to data frame
# convert data frame to dict using dict comprehension

# get user input
# print new list content nato alphabet words for each letter that user input in

import pandas

#
data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_code = {row.letter.lower(): row.code for index, row in data.iterrows()}

name = input("Type your name: ")
code_list = [letter_code[letter.lower()] for letter in name]
print(code_list)

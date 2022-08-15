import pandas

# with open("file1.txt", mode="r") as file1:
#     file1_data = file1.readlines()
#
# with open("file2.txt", mode="r") as file2:
#     file2_data = file2.readlines()
#
# list_common = [int(num) for num in file1_data if num in file2_data]
# print(list_common)

# list_common = [int(num) for num in list1 if num in list2]
# print(list_common)

# Dictionary comprehension

# from random import randint
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student:randint(0, 100) for student in names}
# print(student_scores)
# passed_students = {student:score for student, score in student_scores.items() if score > 50}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words_list = sentence.split()
# print(words_list)
#
# word_num_char = {word: len(word) for word in words_list}
# print(word_num_char)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


weather_k = {day: c_to_f(temp_c=temp) for day, temp in weather_c.items()}
print(weather_k)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(f"{key}\n{value}")


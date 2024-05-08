# FILE_NAME_1 = "known1"
# FILE_NAME_2 = "known2"
# FILE_NAME_3 = "known_diff"
FILE_NAME_1 = "learning1"
FILE_NAME_2 = "learning2"
FILE_NAME_3 = "learning_diff"
FILE_1 = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_61\{FILE_NAME_1}.txt"
FILE_2 = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_61\{FILE_NAME_2}.txt"
FILE_3 = fr"C:\Users\Hii\PycharmProjects\100daysofCode\Day_61\{FILE_NAME_3}.txt"
with open(FILE_1, mode="r", encoding="utf-8") as file_1:
    str1 = file_1.read()
with open(FILE_2, mode="r", encoding="utf-8") as file_2:
    str2 = file_2.read()
list1 = str1.split("\n")
print(len(list1))
list2 = str2.split("\n")
print(len(list2))
list_diff = list(set(list1) - set(list2))

with open(FILE_3, mode="w", encoding="utf-8") as file_3:
    for element in list_diff:
        if element[-1] == "다":
            file_3.write(element[:-1] + "고자")
            file_3.write("\n")
        else:
            file_3.write(element + "에게")
            file_3.write("\n")

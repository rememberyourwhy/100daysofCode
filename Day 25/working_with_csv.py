# with open("weather-data.csv", mode="r") as data:
#     list_of_weather = data.read().split("\n")
# print(list_of_weather)


# import csv
# with open("weather-data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import numpy as np

# data = pandas.read_csv("weather-data.csv")

# # Two main datatype
# # DataFrame class. --- similar to spreadsheet
# # try print type(data)
# # Series class. --- similar to a column in a spreadsheet
#
# # pandas features many methods to convert to dif datatype
# # for example: dict, sql, excel
#
# data_dict = data.to_dict()
# print(data_dict)
#
#
# # getting average_temp
# temp_list = data["temp"].to_list()
# average_temp = int(sum(temp_list) / len(temp_list))
# print(average_temp)
# # getting average_temp with pandas
# print(int(data["temp"].mean()))
#
#
# # getting max from a series
# print(data["temp"].max())
#
#
# # get data in column
# print(data["condition"])
# data.condition
# # get data in row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["A", "B", "C"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("squirrel_data.csv")
color_list = squirrel_data["Primary Fur Color"].to_list()
color_dict = {}
for squirrel_color in color_list:
    if squirrel_color not in color_dict.keys():
        color_dict[squirrel_color] = 1
    else:
        color_dict[squirrel_color] += 1
print(color_dict)

# note that we have a NaN key here in our color_dict
# should change it to a more comprehensive key
# the method:
# Method 1:
# dictionary[new_key] = dictionary.pop(old_key)
# Example:
# color_dict["Color is Unknown"] = color_dict.pop(nan)
# Method 2:
# dictionary[new_key] = dictionary[old_key]
# del dictionary[old_key]
# Example
# color_dict["Color is Unknown"] = color_dict[np.nan]
# del color_dict[np.nan]
# Look like both change new_key position in the dictionary
# So we come up with the third solution for this which preserve the order, but we have to rebuild the dictionary
# Example:
# >>> d = {0:0, 1:1, 2:2, 3:3}
# >>> {"two" if k == 2 else k:v for k,v in d.items()}
# {0: 0, 1: 1, 'two': 2, 3: 3}

# I'll use this one since order is not important here
color_dict["Color is Unknown"] = color_dict.pop(np.nan)


keys_list = ["color", "number"]
values_list = [list(color_dict.keys()), list(color_dict.values())]
color_dict_right_format = {keys_list[_]: values_list[_] for _ in range(len(keys_list))}

color_data = pandas.DataFrame(color_dict_right_format)
print(color_data)
color_data.to_csv("squirrel_color_data.csv")

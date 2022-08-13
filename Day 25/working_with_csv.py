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

data = pandas.read_csv("weather-data.csv")

# Two main datatype
# DataFrame class. --- similar to spreadsheet
# try print type(data)
# Series class. --- similar to a column in a spreadsheet

# pandas features many methods to convert to dif datatypes
# for example: dict, sql, excel

data_dict = data.to_dict()
print(data_dict)


# getting average_temp
temp_list = data["temp"].to_list()
average_temp = int(sum(temp_list) / len(temp_list))
print(average_temp)
# getting average_temp with pandas
print(int(data["temp"].mean()))
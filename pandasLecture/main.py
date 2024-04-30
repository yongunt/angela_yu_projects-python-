# with open("weather_data.csv") as csv_data:
#     my_data = csv_data.readlines()
#     print(my_data)
#
# import csv
#
# with open("weather_data.csv") as csv_data:
#     my_data = csv.reader(csv_data)
#     temperatures = []
#     for row in my_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()

# average = round(sum(data_list)/len(data_list), 2)
#
# print(average)

# print(data["temp"].mean())
#
# print(data["temp"].max())

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
#
# print((monday_temp * 9/5) + 32)

#
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


squ_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squ_list = squ_data["Primary Fur Color"].to_list()

black = 0
gray = 0
red = 0

for i in squ_list:
    if i == "Black":
        black += 1
    if i == "Gray":
        gray += 1
    if i == "Cinnamon":
        red += 1

squ_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black]
}

data = pd.DataFrame(squ_dict)

data.to_csv("squirrel_count.csv")

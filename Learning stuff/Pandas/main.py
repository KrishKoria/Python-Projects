# import csv
#
# with open("weather_data.csv", "r") as file:
#     content = csv.reader(file)
#     temps = []
#     for row in content:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#
#     print(temps)
import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data["temp"])
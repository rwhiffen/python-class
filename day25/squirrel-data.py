# Rich Whiffen - 9/26/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 25 - working with csv, data frames and pandas
#


#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

my_data_frame = pandas.DataFrame(data_dict)
my_data_frame.to_csv("squirrel_count.csv")



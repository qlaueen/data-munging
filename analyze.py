# Place code below to do the analysis part of the assignment.

import csv

#read the clean data file
f = open("clean_data.csv",encoding="utf_8")
csv_reader = csv.DictReader(f)

#indicator for separating years from different decades
for year in csv_reader:
    decade=year["Year"][0:3]
    break
#number of years counted per decade
count = 0
temp_sum = 0
for year in csv_reader:
    if year["Year"][0:3] == decade:
        count +=1
        temp_sum += float(year["J-D"])
    else:
        print("Average temperature from {:s}0 to {:s}9:".format(decade,decade)+" {:.1f}".format(temp_sum/count))
        count = 1
        temp_sum = float(year["J-D"])
        decade = year["Year"][0:3]
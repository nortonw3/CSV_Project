# Author:                 Will Norton
# Project Name:           CSV_Project
# File Name:              csv_temps_5.py
# Date Created:           1/20/2020
# Date Last Modified:     1/30/2020
# Description:            The goal of this project is to use matplotlib to graph
#                         temperatures of two locations based on the cooresponding
#                         csv files

import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Open files and set to read only
open_file_dv = open("death_valley_2018_simple.csv", "r" )
open_file_sk = open("sitka_weather_2018_simple.csv", "r" )

csv_file_dv = csv.reader(open_file_dv, delimiter=",")
csv_file_sk = csv.reader(open_file_sk, delimiter=",")

# Skip the first line of each file
header_row_dv = next(csv_file_dv)
header_row_sk = next(csv_file_sk)

# Determine the indexes for what data we want
max_i_dv = 0
min_i_dv = 0
date_i_dv = 0
name_i_dv = 0

max_i_sk = 0
min_i_sk = 0
date_i_sk = 0
name_i_sk = 0

for index, column_header in enumerate(header_row_dv):
    if column_header == 'NAME':
        name_i_dv = index
    elif column_header == 'DATE':
        date_i_dv = index
    elif column_header == 'TMAX':
        max_i_dv = index
    elif column_header == 'TMIN':
        min_i_dv = index
    #print(index, column_header)
print('Death Valley')
print('NAME index: ' + str(name_i_dv))
print('DATE index: ' + str(date_i_dv))
print('TMAX index: ' + str(max_i_dv))
print('TMIN index: ' + str(min_i_dv) + '\n')


for index, column_header in enumerate(header_row_sk):
    if column_header == 'NAME':
        name_i_sk = index
    elif column_header == 'DATE':
        date_i_sk = index
    elif column_header == 'TMAX':
        max_i_sk = index
    elif column_header == 'TMIN':
        min_i_sk = index
    #print(index, column_header)
print('Sitka Airport')
print('NAME index: ' + str(name_i_sk))
print('DATE index: ' + str(date_i_sk))
print('TMAX index: ' + str(max_i_sk))
print('TMIN index: ' + str(min_i_sk))

print('\n')

# Create Lists to store data from each file
highs_dv = [] 
lows_dv = []
dates_dv = []
names_dv = []

highs_sk = [] 
lows_sk = []
dates_sk = []
names_sk = []

# Loop through each file line by line and append lists with data
for row in csv_file_dv:
    try:
        high = int(row[max_i_dv])
        low = int(row[min_i_dv])
        current_date = datetime.strptime(row[date_i_dv], '%Y-%m-%d')
        name = row[name_i_dv]
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(current_date)
        names_dv.append(name)

for row in csv_file_sk:
    try:
        high = int(row[max_i_sk])
        low = int(row[min_i_sk])
        current_date = datetime.strptime(row[date_i_sk], '%Y-%m-%d')
        name = row[name_i_sk]
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs_sk.append(high)
        lows_sk.append(low)
        dates_sk.append(current_date)
        names_sk.append(name)

#print(list(names_dv))
#print(list(names_sk))

# Graph formatting
#fig = plt.figure()
fig, (sk, dv) = plt.subplots(nrows=2, ncols=1, sharex=True)

dv.plot(dates_dv, highs_dv, color='red', alpha=0.5)
dv.plot(dates_dv, lows_dv, color='blue', alpha=0.5)

sk.plot(dates_sk, highs_sk, color='red', alpha=0.5)
sk.plot(dates_sk, lows_sk, color='blue', alpha=0.5)

dv.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
sk.fill_between(dates_sk, highs_sk, lows_sk , facecolor='blue', alpha=0.1)

dv.set_title(names_dv[0], fontsize=12)
dv.set_xlabel("", fontsize=10)
dv.set_ylabel("Temperature (F)", fontsize=10)
dv.tick_params(axis="both", which="major", labelsize=10)

sk.set_title(names_sk[0], fontsize=12)
sk.set_xlabel("", fontsize=10)
sk.set_ylabel("Temperature (F)", fontsize=10)
sk.tick_params(axis="both", which="major", labelsize=10)

fig.suptitle(f"Temperature comparison between {names_sk[0]} and {names_dv[0]}", fontsize=12)

fig.autofmt_xdate()

# Close files
open_file_dv.close()
open_file_sk.close()

# Show Plot
plt.show()
    
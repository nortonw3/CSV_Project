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
print('Death Valley')
for index,column_header in enumerate(header_row_dv):
    print(index, column_header)

print('\nSitka')
for index,column_header in enumerate(header_row_sk):
    print(index, column_header)

print('\n')

# Create Lists to store data from each file
highs_dv = [] 
lows_dv = []
dates_dv = []

highs_sk = [] 
lows_sk = []
dates_sk = []

# Loop through each file line by line and append lists with data
while True:
    try:
        for row in csv_file_dv:
            highs_dv.append(int(row[4]))
            #print(row[5])
            lows_dv.append(int(row[5]))
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates_dv.append(current_date)
        
        for row in csv_file_sk:
            highs_sk.append(int(row[5]))
            #print(row[5])
            lows_sk.append(int(row[6]))
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates_sk.append(current_date)

# Catch any row with incorrect data and continue appending lists
    except ValueError as e:
        print(e, row)
        continue 

# exit loop when done
    break

# Graph formatting
#fig = plt.figure()
fig, (sk, dv) = plt.subplots(nrows=2, ncols=1, sharex=True)

dv.plot(dates_dv, highs_dv, color='red', alpha=0.5)
dv.plot(dates_dv, lows_dv, color='blue', alpha=0.5)

sk.plot(dates_sk, highs_sk, color='red', alpha=0.5)
sk.plot(dates_sk, lows_sk, color='blue', alpha=0.5)

dv.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
sk.fill_between(dates_sk, highs_sk, lows_sk , facecolor='blue', alpha=0.1)

dv.set_title("DEATH VALLEY, CA US", fontsize=12)
dv.set_xlabel("", fontsize=10)
dv.set_ylabel("Temperature (F)", fontsize=10)
dv.tick_params(axis="both", which="major", labelsize=10)

sk.set_title("SITKA AIRPORT, AK US", fontsize=12)
sk.set_xlabel("", fontsize=10)
sk.set_ylabel("Temperature (F)", fontsize=10)
sk.tick_params(axis="both", which="major", labelsize=10)

fig.suptitle("Temperature comparison between Sitka Airport, AK US and Death Valley, CA US", fontsize=12)

fig.autofmt_xdate()

# Close files
open_file_dv.close()
open_file_sk.close()

# Show Plot
plt.show()
    
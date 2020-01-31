import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r" )

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index, column_header)

highs = [] 
lows = []
dates = []

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    

#print(highs[:10])

fig = plt.figure()

plt.plot(dates, highs, color='red', alpha=0.5)
plt.plot(dates, lows, color='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high temps for Death Valley 2018", fontsize=16)
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

plt.show()
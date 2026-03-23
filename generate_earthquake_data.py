import csv
import random
from datetime import datetime, timedelta

header = ["date","time","latitude","longitude","depth","magnitude","mag_type","place"]
rows = []

# Start from the last date in your current data, or just pick a base date
date_base = datetime(2024, 2, 1)

for i in range(10000):
    date = (date_base + timedelta(days=i)).strftime("%Y-%m-%d")
    time = f"{random.randint(0,23):02}:{random.randint(0,59):02}:{random.randint(0,59):02}"
    latitude = round(random.uniform(-90, 90), 2)
    longitude = round(random.uniform(-180, 180), 2)
    depth = round(random.uniform(0, 100), 2)
    magnitude = round(random.uniform(2.0, 7.0), 2)
    mag_type = "ml"
    place = f"place{i+100}"
    rows.append([date, time, latitude, longitude, depth, magnitude, mag_type, place])

with open("earthquake_data.csv", "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Added 10,000 new rows to earthquake_data.csv")

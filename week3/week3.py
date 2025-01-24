import ssl
import urllib.request as request
import json
import csv
import os

# ssl problem
ssl._create_default_https_context = ssl._create_unverified_context

# Fetch data from URLs
url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

def fetch_data(url):
    with request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

data1 = fetch_data(url1)["data"]["results"]
data2 = fetch_data(url2)["data"]

# print(data)
# print(data1)

# Extract districts from address
valid_districts = [
    "中正區", "萬華區", "中山區", "大同區", "大安區", 
    "松山區", "信義區", "士林區", "文山區", "北投區", 
    "內湖區", "南港區"
]

# create spot.csv
with open("spot.csv", "w", encoding="utf-8") as spot_file:
    for spot_title in data1:
        spot_file.write(spot_title["stitle"]+"\n")
    # writer = csv.writer(spot_file)
    # writer.writerow(["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"])

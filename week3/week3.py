import ssl
import urllib.request as request
import json
import csv

# ssl problem
# ssl._create_default_https_context = ssl._create_unverified_context

# Fetch data from URLs
url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

def fetch_data(url):
    with request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

data1 = fetch_data(url1)["data"]["results"]
data2 = fetch_data(url2)["data"]

# # print(data)
# # print(data1)

# # Extract districts from address
# valid_districts = [
#     "中正區", "萬華區", "中山區", "大同區", "大安區", 
#     "松山區", "信義區", "士林區", "文山區", "北投區", 
#     "內湖區", "南港區"
# ]

# # find district by SERIAL_NO
# def find_district(serial_no):
#     for item in data2:
#         if item["SERIAL_NO"] == serial_no:
#             address = item.get("address", None)
#             for district in valid_districts:
#                 if district in address:
#                     return district
#     return ""


# # create spot.csv
# with open("spot.csv", "w", encoding="utf-8", newline="") as spot_file:
#     writer = csv.writer(spot_file)

#     for item in data1:
#         SpotTitle = item["stitle"]
#         Serial_NO = item["SERIAL_NO"]
#         Longitude = item["longitude"]
#         Latitude = item["latitude"]
#         Image_URL = item["filelist"].split("http")[1]
#         Image_URL = f"http{Image_URL}" 
#         District = find_district(Serial_NO)
#         writer.writerow([SpotTitle, District, Longitude, Latitude, Image_URL])


# # Group dict for mrt.csv
# serial_to_stitle = {item["SERIAL_NO"]: item["stitle"] for item in data1}

# # create mrt.csv
# with open("mrt.csv", "w", encoding="utf-8", newline="") as mrt_file:
#     writer = csv.writer(mrt_file)
    
#     # 建立空字典，將匹對到的資料存入
#     mrt_to_stitles = {}
#     for item in data2:
#         mrt = item["MRT"]
#         serial_no = item["SERIAL_NO"]
        
#         # 加入 SERIAL_NO 有對應的 stitle
#         if serial_no in serial_to_stitle:
#             if mrt not in mrt_to_stitles:
#                 mrt_to_stitles[mrt] = []
#             mrt_to_stitles[mrt].append(serial_to_stitle[serial_no])
    
#     for mrt, stitles in mrt_to_stitles.items():
#         writer.writerow([mrt, *stitles])

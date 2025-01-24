import csv
import json
import urllib.request as request
src="https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") 
data = json.loads(data)
print(data)


# # URLs for data
# data_urls = [
#     "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1",
#     "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
# ]

# # Districts to extract from address
# districts = [
#     "中正區", "萬華區", "中山區", "大同區", "大安區", "松山區",
#     "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"
# ]

# # Function to extract district from address
# def extract_district(address):
#     for district in districts:
#         if district in address:
#             return district
#     return "Unknown"

# # Fetch and parse data
# data = []
# for url in data_urls:
#     with urllib.request.urlopen(url) as response:
#         source_data = json.load(response)
#         data.extend(source_data["result"].get("results", []))

# # Create spot.csv
# with open("spot.csv", "w", newline="", encoding="utf-8") as spot_file:
#     writer = csv.writer(spot_file)
#     writer.writerow(["SpotTitle", "District", "Longitude", "Latitude", "ImageURL"])

#     for item in data:
#         title = item.get("stitle", "")
#         address = item.get("address", "")
#         district = extract_district(address)
#         longitude = item.get("longitude", "")
#         latitude = item.get("latitude", "")
#         images = item.get("filelist", "").split("http")
#         image_url = f"http{images[1]}" if len(images) > 1 else ""

#         writer.writerow([title, district, longitude, latitude, image_url])

# # Group data by MRT station
# mrt_data = {}
# for item in data:
#     mrt_station = item.get("MRT", "Unknown")
#     title = item.get("stitle", "")

#     if mrt_station not in mrt_data:
#         mrt_data[mrt_station] = []
#     mrt_data[mrt_station].append(title)

# # Create mrt.csv
# with open("mrt.csv", "w", newline="", encoding="utf-8") as mrt_file:
#     writer = csv.writer(mrt_file)
#     for station, spots in mrt_data.items():
#         writer.writerow([station] + spots)

# print("Files 'spot.csv' and 'mrt.csv' have been generated.")

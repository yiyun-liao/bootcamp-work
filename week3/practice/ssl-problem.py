# 一般的寫法 ###################################
import csv
import json
import urllib.request as request
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") 
data = json.loads(data)
print(data)


# 繞過 ssl 問題 ###################################
import ssl
import urllib.request as request
import json
import csv
import os

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"

with request.urlopen(src) as response:
    data = response.read().decode("utf-8") 
data = json.loads(data)
# print(data)

spot_data = data["data"]["results"]
# print(spot_data)


# 看不懂的高級寫法 ###################################
# import json
# from urllib.request import urlopen, Request
# from urllib.error import HTTPError, URLError

# headers = {
#     "User-Agent": "Python/urllib",
#     "Accept": "application/json",
#     "Connection": "keep-alive"
# }

# def get(url, headers=None):
#     """
#     使用 urllib.request 發送 GET 請求，並返回 JSON 格式的響應數據。
#     :param url: 請求的 URL
#     :param headers: 請求的自定義 Headers (選填)
#     :return: dict or list - JSON 解碼的 Python 對象
#     """
#     try:
#         # 建立 Request 對象
#         request = Request(url, headers=headers or {})
        
#         # 發送請求
#         with urlopen(request) as response:
#             # 讀取響應並解碼
#             response_data = response.read().decode('utf-8')
            
#             # 將響應數據轉換為 JSON 格式
#             json_data = json.loads(response_data)
#             return json_data

#     except HTTPError as e:
#         print(f"HTTP error occurred: {e.code} - {e.reason}")
#     except URLError as e:
#         print(f"URL error occurred: {e.reason}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

#     return None

# url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
# data = get(url, headers) 
# print(data)


# mrt.csv 個別印出對應捷運跟景點名稱
創建 mrt.csv
with open("mrt.csv", "w", encoding="utf-8", newline="") as mrt_file:
    writer = csv.writer(mrt_file)
    
    # 寫入表頭
    writer.writerow(["MRT", "stitle1", "stitle2", "stitle3", "..."])
    
    for mrt_entry in data2:
        mrt = mrt_entry.get("MRT", "Unknown MRT")  # MRT 名稱
        serial_no = mrt_entry.get("SERIAL_NO")    # SERIAL_NO
        if not serial_no:
            continue  # 如果 SERIAL_NO 不存在，跳過該條目
        
        # 找到 SERIAL_NO 對應的所有 stitle
        stitles = [serial_to_stitle[serial_no]] if serial_no in serial_to_stitle else []
        
        # 寫入行（MRT 和 stitle 集合）
        writer.writerow([mrt, *stitles])
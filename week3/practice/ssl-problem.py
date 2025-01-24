# import csv
# import json
# import urllib.request as request
# src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8") 
# data = json.loads(data)
# print(data)


import ssl
import urllib.request as request

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") 
print(data)

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


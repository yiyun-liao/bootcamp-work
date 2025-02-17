# urllib.request.urlopen() ================================================================================
import urllib.request as req
import ssl
import bs4

url="https://www.ptt.cc/bbs/movie/index.html"

ssl._create_default_https_context = ssl._create_unverified_context

# 建立 request 物件，附加 Request Headers 資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 解析原始碼，取得每篇文章的標題
root=bs4.BeautifulSoup(data, "html.parser")
print(root.title.string)
# 尋找 class="title" 的 div 標籤
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a and title.a.string:
        print(title.a.string)
    else:
        print("本文已被刪除")


# requests.get() ================================================================================
import requests
import bs4

url = "https://www.ptt.cc/bbs/movie/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)
data = response.text

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")

for title in titles:
    if title.a:
        print(title.a.string)
    else:
        print("本文已被刪除")
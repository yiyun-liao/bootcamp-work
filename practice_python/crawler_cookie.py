# urllib.request.urlopen() ================================================================================
import urllib.request as req
import ssl
import bs4

ssl._create_default_https_context = ssl._create_unverified_context

# crawler 見 practice_python/crawler.py
def getData(url):
    # 看 cookie
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    }) 
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    for title in titles:
        if title.a and title.a.string:
            print(title.a.string)
        else:
            print("本文已被刪除")
     
    # 找到「上頁」按鈕，並且 return 出來
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]


pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
# print(pageURL)
count = 0
while count < 3:
    print(f"第{count}頁資料==========================================================")
    pageURL="https://www.ptt.cc" + getData(pageURL)
    count +=1

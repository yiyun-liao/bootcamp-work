import urllib.request as req
import ssl
import json

url="https://medium.com/_/graphql"

ssl._create_default_https_context = ssl._create_unverified_context

request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

data=data.replace("])}while(1);</x>", "") #因為 medium 自身的寫法含有此串字串，所以把他們移除
data=json.loads(data)
print(data)

# 取得 JSON 資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])
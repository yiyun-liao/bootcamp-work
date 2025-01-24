import ssl
import urllib.request as request

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") 
print(data)

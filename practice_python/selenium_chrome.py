# 使用 webdriver-manager 自動安裝 ============================================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 自動下載並使用適合的 chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 開啟 Google 首頁
driver.get("https://www.google.com")
print("連線成功")
driver.maximize_window() #視窗最大化
driver.save_screenshot("screenShot.png")
driver.get("https://tw.amazingtalker.com/")
driver.save_screenshot("at.png")
# 等待 5 秒
import time
time.sleep(5)

# 關閉瀏覽器
driver.quit()

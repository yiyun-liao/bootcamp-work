from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.ptt.cc/bbs/stock/index.html")

# 連續取 3 頁內容
# count = 0
# while count < 3:
#     print(f"第{count}頁資料==========================================================")
#     element = driver.find_elements(By.CLASS_NAME,"title")
#     for e in element:
#         print(e.text)
#     next_page= driver.find_element(By.LINK_TEXT, "‹ 上頁")
#     next_page.click()
#     count += 1

# 連續取 3 頁內容
target_keyword = "川普"
max_pages = 3  # 最多搜尋 3 頁
current_page = 0  # 記錄目前頁數

while current_page < max_pages:
    print(f"第{current_page}頁資料==========================================================")
    elements = driver.find_elements(By.CLASS_NAME,"title")
    for e in elements:
        title = e.text.strip()
        print(title)
        if target_keyword in title:
            print(f"找到包含 {target_keyword} 的文章，停止搜尋！")
            driver.quit()
            exit()
    try:
        next_page= driver.find_element(By.LINK_TEXT, "‹ 上頁")
        next_page.click()
        current_page += 1
    except:
        print("找不到『上頁』按鈕，結束搜尋")
        break

time.sleep(5)
driver.quit()
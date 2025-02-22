from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

leeCode_username = os.getenv("leeCodeUserName")
leeCode_password = os.getenv("leeCodePassword")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://leetcode.com/accounts/login/")
time.sleep(5)

# signin
userName_input=driver.find_element(By.ID,"id_login")
password_input=driver.find_element(By.ID,"id_password")
userName_input.send_keys(leeCode_username)
password_input.send_keys(leeCode_password)
# 這邊有錯 qq
human_check=driver.find_element(By.ID, "cf-chl-widget-19z7s")
signin_btn=driver.find_element(By.ID, "signin_btn")

time.sleep(2)
human_check.send_keys(Keys.ENTER)
time.sleep(1)
signin_btn.send_keys(Keys.ENTER)
time.sleep(5)

# get value
driver.get("https://leetcode.com/problemset/")
time.sleep(3)
statElement=driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
print(statElement.text)

columns = statElement.text.split("/n")
print("已完成刷題數量：", columns[1])


driver.quit()
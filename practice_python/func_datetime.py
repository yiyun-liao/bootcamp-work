from datetime import date, timedelta, datetime, timezone

# 取得資訊
dt = date.today()
print(dt) # 2025-02-22
print(dt.year, dt.month, dt.day) # 2025 2 22
print("星期幾：", dt.weekday()) # 5

# 指定日期
dt1 = date(2025,1,1)
print(dt1) # 2025-01-01
print("星期幾：", dt1.weekday()) # 2

# 日期增減
dt2 = date.today() # 2025-02-22
differ = timedelta(weeks=1)
after_week_date = dt + differ
print(after_week_date) # 2025-03-01

# 印出本月份所有日期跟星期
today = date.today() 
dt3=date(today.year, today.month, 1,)
weekday_name={
    0:"週一", 1:"週二", 2:"週三", 3:"週四", 4:"週五", 5:"週六", 6:"週日"
}
while dt3.month == today.month:
    print("一整個月：", dt3, weekday_name[dt3.weekday()])
    dt3 += timedelta(days=1)

# 取得時間資訊
dt4 = datetime.now()
print(dt4.year, dt4.month, dt4.day, dt4.hour, dt4.minute, dt4.second)
print("星期幾：", dt4.weekday())

# 指定日期
dt6 = datetime(2025,1,1,12,34,34)
print(dt6) # 2025-01-01 12:34:34
print("星期幾：", dt6.weekday()) # 2

# 時間增加 8 小時 30 分鐘
dt7 = datetime.now() # 2025 2 22 16 4 44
differ2 = timedelta(hours=8, minutes=30)
new_time = dt7 + differ2
print(new_time) # 2025-02-23 00:34:44.136651

# 操作時區類別
# 日本(+9),台灣(+8)
jp_tz = timezone(timedelta(hours=9))
tw_tz = timezone(timedelta(hours=8))
tw_now=datetime.now() # 不用特別設定，因為目前就是在台灣
print(tw_now)
jp_now=datetime.now(jp_tz) #要顯示日本時間，需要帶入時差物件
print(jp_now)
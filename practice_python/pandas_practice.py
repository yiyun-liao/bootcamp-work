import pandas as pd

# Series
data=pd.Series([20,10,15])
# print("Max", data.max())
# print("Median",data.median())
dataDouble=data*2
# print("dataDouble", dataDouble)

# 比較運算
data=data==20 #逐一比較是否 == 20
print(data)

# DataFrame
data=pd.DataFrame({
    "Name":["Amy", "Nick", "Tom"],
    "Age":[18, 17, 24]
})
# print(data)
# 取得特定欄位
print(data["Name"])
print(data.iloc[0])


# pure python================================================================================
data = [20, 10, 15]

# Max
max_value = max(data)
# print("Max(pure):", max_value)

# Median (中位數)
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 1:  # 奇數個數
    median_value = sorted_data[n // 2] #整數除法 (//) 
else:  # 偶數個數
    median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
# print("Median(pure):", median_value)

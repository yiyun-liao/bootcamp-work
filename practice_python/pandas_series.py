import pandas as pd

data=pd.Series([5,4,-1,3,7],index=["a","b","c","d","e"])

print("資料型態：", data.dtype)
print("資料數量：", data.size)
print("資料索引：", data.index)
print("第二筆資料：", data[1])
print("索引 e 的資料：", data["e"])
print("總和：", data.sum())
print("最大值：", data.max())
print("乘法總和：", data.prod())
print("平均數：", data.mean())
print("中位數：", data.median())
print("標準差：", data.std())
print("最大的兩個數：", data.nlargest(2), sep="\n")
print("最小的兩個數：", data.nsmallest(2), sep="\n")

data2=pd.Series(["您好", "Python", "Pandas"])
print("全部變小寫：", data2.str.lower(), sep="\n")
print("全部變大寫：", data2.str.upper(), sep="\n")
print("計算每個字串長度：", data2.str.len(), sep="\n")
print("串成一個字串：", data2.str.cat(sep=","))
print("判斷字串是否包含大寫 P：", data2.str.contains("P"), sep="\n")
print("把您好取代成 Hello：", data2.str.replace("您好", "Hello"), sep="\n")

# 建立篩選條件
data3=pd.Series([30, 15, 20])
condition1=[True, False, True]
filteredData1=data3[condition1]
print("取第一筆及第三筆資料：", filteredData1, sep="\n")
condition2=data3>18
filteredData2=data3[condition2]
print("值大於 18 ：", filteredData2, sep="\n")

# string 建立篩選條件
data4=pd.Series(["您好", "Python", "Pandas"])
condition3=data.str.contains("P")
print(condition3) #跟上方不同的是這邊有經過運算
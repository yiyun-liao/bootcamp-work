import pandas as pd

data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[300000, 400000, 500000],
},index=["a", "b", "c"])

print("資料數列：", data.size)
print("資料型態（列, 欄）：", data.shape)
print("資料索引：", data.index)
print("取得第二列：", data.iloc[1], sep="\n")
print("取得第 c 列：", data.loc["c"], sep="\n")
print("取得第二欄：", data["name"], sep="\n") 

#取出一欄資料當作 Series 處理
names = data["name"] 
print("取出 dataFrame 作為 Series 使用：", names.str.upper(), sep="\n")
salaries = data["salary"]
print("薪水總支出：", salaries.sum())

#取出一列資料當作 Series 處理
payslip = data.loc["a"]
print("c 員工薪資條：", payslip["name"],":",payslip["salary"])


# 新增欄位
data["revenue"]=[500000, 400000, 300000]
print("新增欄位：", data, sep="\n")
# 新增欄位= Series 名稱(依循 index)
data["rank"]=pd.Series([3,6,1], index=["a","c","b"])
print("新增 Series：", data, sep="\n")

# 常見用法
data["cp"]=data["revenue"]/data["salary"]
print("誰 cp 值高：", data, sep="\n")


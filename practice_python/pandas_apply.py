import pandas as pd

# 讀取資料================================================================================================================================================================
data=pd.read_csv("practice_python/googleplaystore.csv") # 把 csv 格式的檔案讀成一個 DataFrame

# 觀察資料================================================================================================================================================================
print("資料數量：", data.shape, sep="\n")
print("資料數量：", data.columns, sep="\n")

# 分析資料：評分各種統計數據==================================================================================================================================================

print("前 100 筆資料的平均數：", data["Rating"].nlargest(100).mean()) #平均數： 5.14 發現資料有問題

condition1=data["Rating"]>5
debug=data[condition1]
# print(debug) # 發現資料問題，重新篩選

condition2=data["Rating"]<=5
realData=data[condition2]
print("平均數：", realData["Rating"].mean())
print("中位數：", realData["Rating"].median())
print("前 1000 筆資料的平均數(更新後)：", realData["Rating"].nlargest(1000).mean())

# 分析資料：安裝數量的各種統計數據================================================================================================================================================
# print("安裝數量：", Data["Installs"]) # 發現是字串
#將資料從字串轉成數字再覆蓋回原本欄位中，一個一個調整，移除 , +，移除特別資料
data["Installs"] = data["Installs"].str.replace(r"[,+]", "", regex=True).str.replace("Free", "", regex=False)
data["Installs"] = pd.to_numeric(data["Installs"])
# print("new",data["Installs"])
condition3=data["Installs"]>1000000
print("安裝數量大於 10 萬的有幾個", data[condition3].shape) # (2832, 13)
print("安裝數量大於 10 萬的有幾個", data[condition3].shape[0]) # 2832

# 基於資料的應用：關鍵字搜尋應用程式名稱==============================================================================================================================================
keyword=input("請輸入關鍵字：")
condition4=data["App"].str.contains(keyword, case=False)
print("符合關鍵字的 app:", data[condition4]["App"])
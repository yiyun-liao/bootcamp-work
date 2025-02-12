import mysql.connector

# 建立連線
con=mysql.connector.connect(
    user="root",
    password="Yiyun4356",
    host="localhost",
    database="practice"
)

print('連線成功')
# 建立 Cursor 物件，用來對資料庫下 SQL 指令
# 將變數資料代入到 SQL 指令裡面
productID=7
productName="奶綠"
cursor=con.cursor()
cursor.execute("INSERT INTO product(id, name) VALUES (%s, %s)",(productID,productName))
con.commit() #確定執行
# 關閉連線
con.close()
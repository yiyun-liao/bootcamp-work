import mysql.connector

# 建立連線
con=mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="practice"
)
print('連線成功')

# 建立 Cursor 物件，用來對資料庫下 SQL 指令
cursor=con.cursor()

# 將變數資料代入到 SQL 指令裡面

#INSERT INTO
# productID=7
# productName="奶綠"
# cursor.execute("INSERT INTO product(id, name) VALUES (%s, %s)",(productID,productName))

#UPDATE
# productName="美式"
# productID=1
# cursor.execute("UPDATE product SET name=%s WHERE id=%s ", (productName, productID))

# 取得多筆資料
# cursor.execute("SELECT * FROM product")
# data=cursor.fetchall()
# print(data)
# #分開取出資料
# for row in data:
#     print(row[0], row[1])

# 取得單筆資料
cursor.execute("SELECT * FROM product WHERE id=2")
data=cursor.fetchone()
print(data)
print(data[0], data[1]) #分開取出資料

#確定執行
con.commit()

# 關閉連線
con.close()
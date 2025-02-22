import csv

# 寫入檔案
with open("data.csv", mode="w", newline="")as file:
    writer=csv.writer(file)
    writer.writerow([1,2,3])
    writer.writerow([4,5,6])
    writer.writerow([7,8,9])

# 讀取檔案
with open("data.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    total = 0
    for r in reader:
        for data in r:
            total += int(data)
    print(total)
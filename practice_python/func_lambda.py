# test1 與 test2 函式相同
# def test1(n1, n2):
#     return n1+ n2
# result1=test1(3,4)

test2 = lambda n1, n2 : n1+n2
result2=test2(3,4)

# 沒有參數
# def test3():
#     return 5*2
# result3=test3()

test4 = lambda : 5*2
result4=test4()

# 不定參數
# def test5(*ns):
#     return max(ns)*2
# result3=test5(1,5,-2)

test6 = lambda *ns : max(ns)*2
result4=test6(1,5,-2)

# filter(函式, 列表)
data=[1,5,-2,10,-5]
filtered_data=filter(lambda n : n>0, data) # 保留大於 0 的值
filtered_list=list(filtered_data)
print(filtered_list)

# map(函式, 列表)
data2=[1,5,-2,10,-5]
filtered_data2=map(lambda n : n*2, data2) # 保留大於 0 的值
filtered_list2=list(filtered_data2)
print(filtered_list2)

# 時間
from datetime import datetime
# def now():
#     return datetime.now()

now=lambda :datetime.now() # 2025-02-22 16:41:27.442009
print(now())
# task1////////////////////////////////////////////////////////////////////////////////
# build data structure
# find the 'station' in messages and return station only (simply the sentence)
# calculate the nearest station
def find_and_print(messages, current_station):
    stations = [
        "Xindian",
        "Xindian City Hall",
        "Qizhang",
        "Dapinglin",
        "Jingmei",
        "Wanlong",
        "Gongguan",
        "Taipower Building",
        "Guting",
        "Chiang Kai-Shek Memorial Hall",
        "Xiaonanmen",
        "Ximen",
        "Beimen",
        "Zhongshan",
        "Songjiang Nanjing",
        "Nanjing Fuxing",
        "Taipei Arena",
        "Nanjing Sanmin",
        "Songshan"
    ]

    # find the 'station' in messages
    # Xiaobitan 先計算為 Qizhang 之後再加一
    # list.append(elmnt)
    friend_locations = []
    for name, message in messages.items():
        for station in stations:
            if "Xiaobitan" in message:
                friend_locations.append({"name": name, "station": "Xiaobitan", "station_value": stations.index("Qizhang")})
            if station in message:
                friend_locations.append({"name": name, "station": station, "station_value": stations.index(station)})
            else:
                friend_locations.append({"name": name, "station": "can't find locate", "station_value": None})

    # 計算與 currentStation 的距離
    if current_station == "Xiaobitan":
        current_station_value = stations.index("Qizhang")
    else:
        current_station_value = stations.index(current_station)


    # find the nearest friend
    closest_friend = None
    min_distance = float('inf')

    for friend in friend_locations:
        if friend["station_value"] is None:
            continue  # 跳過沒有有效車站的朋友 
        distance = abs(friend["station_value"] - current_station_value)
        if friend["station"] == "Xiaobitan":
                distance += 1

        if distance < min_distance:
            min_distance = distance
            closest_friend = friend["name"]

    print(closest_friend)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

# task2////////////////////////////////////////////////////////////////////////////////
# sort by price or rate, get array [teacherA, teacherB, teacherC]
# check time
def book(consultants, hour, duration, criteria):

    #sort by price or rate
    if criteria == "price":
        sorted_consultants = sorted(consultants, key=lambda x: x["price"]) #返回一個新的列表
    elif criteria == "rate":
        def get_rate(x):
            return x["rate"]
        sorted_consultants = sorted(consultants, key=get_rate, reverse=True) #key 參數需要是一個函數，同上面做法
    else:
        print("Invalid criteria")
        return
    
    # check the time
    for consultant in sorted_consultants:
        # Initialize booked array if not already present
        if "booked" not in consultant:
            consultant["booked"] = []
        
        # Check if the time is available
        is_available = True
        for booking in consultant["booked"]:
            if hour < booking["end"] and hour + duration > booking["start"]:
                is_available = False
                break

        # If available, book the time and return the consultant's name
        if is_available:
            consultant["booked"].append({"start": hour, "end": hour + duration})
            print(consultant["name"])
            return
        
    # If no consultants are available
    print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

# task3///////////////////////////////////////////////////////////////////////////////
# step01: choose second word:4in5, 3in4, 2in3, 2in2
# step02: select the different one => which only be counted in one time

def func(*data):
    middle_name_count = {}
    middle_name_map = {}

    #choose second word
    for name in data:
        if len(name) == 2:
            middle_name = name[-1]
        else:
            middle_name = name[-2] #直接取絕對位置，反正就是倒數第二個字
    
        #count the occurrences of the middle name
        #key (明) 如果有值就「值+1」 ，沒有的話「0+1」, middleNameCount = {明：1}
        middle_name_count[middle_name] = middle_name_count.get(middle_name, 0) + 1
        
        # record it and allow to overwrite
        # middleNameMap[明] = 陳王明雅, middleNameMap = {明：陳王明雅}
        middle_name_map[middle_name] = name

    #Find the unique middle name
    unique_middle_name = None
    for key, count in middle_name_count.items():
        if count == 1:
            unique_middle_name = key
            break
    
    if unique_middle_name:
        print(middle_name_map[unique_middle_name])
    else:
        print("沒有")

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

# task4///////////////////////////////////////////////////////////////////////////////
#There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
#rule +4 +4 -1 
#function1: for...in, range()
def get_number(index):
    ans = 0
    for i in range(1, index+1):
        if i % 3 == 0:
            ans -= 1
        else:
            ans += 4
    print(ans)

#function2: calculate: (index)x4-[index/3 取整數]X5
def get_number(index):
    print(index * 4 - (index // 3 * 5))

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70
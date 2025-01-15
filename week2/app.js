// task01
// build data structure
// find the 'station' in messages and return station only (simply the sentence)
// calculate the nearest station
// function findAndPrint(messages,currentStation){
//     const stations = {
//         "01": "Xindian",
//         "02": "Xindian City Hall",
//         "03": "Qizhang",
//         "03.1": "Xiaobitan",
//         "04": "Dapinglin",
//         "05": "Jingmei",
//         "06": "Wanlong",
//         "07": "Gongguan",
//         "08": "Taipower Building",
//         "09": "Guting",
//         "10": "Chiang Kai-Shek Memorial Hall",
//         "11": "Xiaonanmen",
//         "12": "Ximen",
//         "13": "Beimen",
//         "14": "Zhongshan",
//         "15": "Songjiang Nanjing",
//         "16": "Nanjing Fuxing",
//         "17": "Taipei Arena",
//         "18": "Nanjing Sanmin",
//         "19": "Songshan"
//     };

//     const friendsLocation = {};
//     const friendsLocationArr = [];
//     for(const person in messages){
//         for (const stationNumber in stations){
//             if(messages[person].includes(stations[stationNumber])){
//                 friendsLocation[person] = stationNumber; //Convert the metro in the sentence into key.
//                 friendsLocationArr ++;//collect all friendsLocation into array
//             }
//         }
//     }
//     let currentStationNumber = null;
//     for (const stationNumber in stations){
//         if (stations[stationNumber] === currentStation) {
//             currentStationNumber = stationNumber; //Convert currentStations into key.
//             break;
//         }
//     }
//     let nearestPerson = null;
//     let minDistance = Infinity;
//     for (const person in friendsLocation) {
//         const personStationNumber = friendsLocation[person];
//         // 計算兩個站點的數字差距 (處理帶有小數點的編號)
//         const personNumber = parseFloat(personStationNumber); // 轉為浮點數
//         const currentNumber = parseFloat(currentStationNumber); // 轉為浮點數
//         const distance = Math.abs(personNumber - currentNumber); // 計算距離
//         if (distance < minDistance) {
//             minDistance = distance;
//             nearestPerson = person;
//         }
//     }

//     return nearestPerson; // 返回距離最近的人名
// }
// const messages={
//     "Bob":"I'm at Ximen MRT station.",
//     "Mary":"I have a drink near Jingmei MRT station.",
//     "Copper":"I just saw a concert at Taipei Arena.",
//     "Leslie":"I'm at home near Xiaobitan station.",
//     "Vivian":"I'm at Xindian station waiting for you."
// };

// findAndPrint(messages, "Wanlong"); // print Mary
// findAndPrint(messages, "Songshan"); // print Copper
// findAndPrint(messages, "Qizhang"); // print Leslie
// findAndPrint(messages, "Ximen"); // print Bob
// findAndPrint(messages, "Xindian City Hall"); // print Vivian

//task2////////////////////////////////////////////////////////////////////////////////
//sort by price or rate, get array [teacherA, teacherB, teacherC]
//check time
function book(consultants, hour, duration, criteria) {
    let sortedConsultants = [];
  
    //sort by price or rate, get array use: Array.prototype.sort([compareFunction])
    if (criteria === "price") {
      sortedConsultants = consultants.sort((a, b) => a.price - b.price); 
    } else if (criteria === "rate") {
      sortedConsultants = consultants.sort((a, b) => b.rate - a.rate);
    }
  
    for (let consultant of sortedConsultants) {
        // Add booked in array, booked is also an array. 
        // Cause next student should check the available time, we should add value in consultants
        // BTW: why do use 'if', cause the function wil run in every time
        if (!consultant.booked){
            consultant.booked = [];
        } 
  
        // Check whether the time is available, if not, just check another teacher
        let isAvailable = true;
        for (let booking of consultant.booked) {
        if (hour < booking.end && hour + duration > booking.start) {
            isAvailable = false; 
            break;
        }
        }
  
        // If yes, add into array and return their name
        if (isAvailable) {
            consultant.booked.push({ start: hour, end: hour + duration });
            console.log(consultant.name);
            return;
        }
    }
  
    // If no available consultants, return "No Service"
    console.log("No Service");
}
  
const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// note: 被預約的時間個別顯示，這樣資料之後還可以被應用，但如果直接合併成時間段，要應用就可能還要再拆開
// consultant=[
//     {"booked":[{"start": 15, "end": 16}, {"start": 11, "end": 13}], "name":"Jenny", "price":800, "rate":3.8},
//     {"booked":[{"start": 10, "end": 12}, {"start": 20, "end": 22}, {"start": 14, "end": 17}], "name":"John", "rate":4.5, "price":1000},
//     {"booked":[{"start": 11, "end": 12}], "name":"Bob", "rate":3, "price":1200},
// ]


//task3///////////////////////////////////////////////////////////////////////////////
// function1: choose second word:4in5, 3in4, 2in3, 2in2 => 這個才有邏輯，取 n-1 
// function2: add string in front of the name, e.g.: A郭林靜宜, AA郭宣恆, AA吳明A => 太複雜了，pass
// select the different one => which only be counted in one time
function func(...data){
    const middleNameCount = {};
    const middleNameMap = {};
  
    // choose second word
    for (let name of data) { 
        let middleName;
        if (name.length === 2) {
            middleName = name[name.length - 1]; // 如果名字只有兩個字，取最後一個字
        } else {
            middleName = name[name.length - 2]; // 取倒數第二個字
        }  

        // count 。 新增進 object 及計算同時進行
        // key (明) 如果有值就「值+1」 ，沒有的話「0+1」, middleNameCount = {明：1}
        middleNameCount[middleName] = (middleNameCount[middleName] || 0) + 1;

        // record it and allow to overwrite
        // middleNameMap[明] = 陳王明雅, middleNameMap = {明：陳王明雅}
        middleNameMap[middleName] = name;
    }
  
    // 找出唯一的中間名
    let uniqueMiddleName = null;
    for (let [key, count] of Object.entries(middleNameCount)) {
      if (count === 1) {
        uniqueMiddleName = key;
        break;
      }
    }
  
    // 輸出結果
    if (uniqueMiddleName) {
      console.log(middleNameMap[uniqueMiddleName]);
    } else {
      console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

//task4///////////////////////////////////////////////////////////////////////////////
//There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
//rule +4 +4 -1 
// function1: build the array and use index to find the value
function getNumber(index){
  let ans = 0;
  for(let i = 1; i <= index; i++){
    if(i % 3 == 0){
      ans -= 1;
    }else{
      ans += 4;
    }
  }
  return console.log(ans);
}

// function2: calculate: (index)x4-[index/3 取整數]X5
function getNumber(index){
  console.log(index * 4 - Math.floor(index / 3) * 5)
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
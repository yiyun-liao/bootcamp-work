//task1////////////////////////////////////////////////////////////////////////////////
// build data structure
// find the 'station' in messages and return station only (simply the sentence)
// calculate the nearest station
// function1: Math.abs(array.key-array.key), Xiaobitan 另外算
function findAndPrint(messages, currentStation){
    
}

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

//task2////////////////////////////////////////////////////////////////////////////////
//sort by price or rate, get array [teacherA, teacherB, teacherC]
//check time
function book(consultants, hour, duration, criteria){
    // your code here
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


//task3///////////////////////////////////////////////////////////////////////////////
// function1: choose second word:4in5, 3in4, 2in3, 2in2 => 這個才有邏輯，取 n-1 
// function2: add string in front of the name, e.g.: A郭林靜宜, AA郭宣恆, AA吳明A
// select the different one => which only be counted in one time
function func(...data){
    // your code here
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
    // your code here
}
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70

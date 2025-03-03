// 資料型態認識 =========================================================================
// let x: number = 3;
// x = true; //compile time error
// let y:string[]=[3, "a", "b"]; //compile time error
// let z:string[]=["3", "a", "b"];


//func =========================================================================
// function show(msg:string){
//     console.log(msg);
// }

// show(5); //compile time error
// show(true); //compile time error
// show("Hello")
// show("Hello", "World") //compile time error


// function add(n1:number, n2:number):number{
//     return n1+n2
// }

// add(3,4)
// add("Hello",5) //compile time error
// add(4) //compile time error
// let ans:string = add(3,4) //compile time error

//定義函式，計算數字陣列總和 =========================================================================
// function calculate(nums:number[]):number{
//     let total = 0 ;
//     for (let i = 0 ; i < nums.length ; i++){
//         total += nums[i];
//     }
//     return total;
// }

// let result:number = calculate([3,4,3,2]);
// console.log(result)


//基本物件資料型態檢查 =========================================================================
// let c ={
//     name:"公司名稱",
//     desc:"寫程式",
//     employees:[
//         {name:"John", role:"manager"},
//         {name:"Mary", role:"fe"}
//     ],
//     size:function(){
//         return this.employees.length;
//     }
// }

// console.log(c.nama, c.desc);  //typo, compile time error
// console.log(c.size * 10000); //not a function, compile time error

//使用 interface =========================================================================
interface Employees{
    name:string; // 用分號
    role:string;
}
interface Company{
    name:string
    desc:string;
    employees: Employees[]; //宣告型態
    size:Function;
}

let c:Company ={  //宣告型態
    name:"公司名稱",
    desc:"寫程式",
    employee:[ //typo, compile time error
        {name:"John", role:"manager"},
        {name:"Mary", role:"fe"}
    ],
    size:function(){
        return this.employees.length;
    }
}

function list(c:Company){
    c.employees.forEach((employee)=>{
        console.log(employee.name, employee.rule); //typo, compile time error
    })
}

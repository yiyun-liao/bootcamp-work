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
function calculate(nums) {
    var total = 0;
    for (var i = 0; i < nums.length; i++) {
        total += nums[i];
    }
    return total;
}
var result = calculate([3, 4, 3, 2]);
console.log(result);

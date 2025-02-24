function echo(msg){
    console.log(msg);
}
let name = "測試會不會衝突";
// export default echo;


let x = 3;
let obj = {x:3, y:4};
let data = [5, 6, 7];
export {x as default, obj, data};
// export default x;
// export {obj, data};

let add = function(n1,n2){
    console.log(n1+n2);
}
let multiply=function(n1,n2){
    console.log(n1*n2);
}
let math={add:add, multiply:multiply}

export {math}; // 包裝
export {add, multiply};

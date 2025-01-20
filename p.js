//[-5, 4, 8, 3, -10]
// 假設資料量是 n
// n*
function test1(arr){
    let max=arr[0]*arr[1]; //1
    for(let i=0 ; i<arr.length ; i++){ //n
        for (let j=i+1 ; j<arr.length ; j++){ //n
            let sum = arr[i] * arr[j]; //1
            if (sum > max){ //1
                max = sum //1
            }
        }
    }
}

function test2(arr){
    let sortedArr = arr.sort((a,b)=> (a-b));
    if(sortedArr[0] * sortedArr[1] > sortedArr[sortedArr.length - 1] * sortedArr[sortedArr.length - 2]){
        console.log(sortedArr[0] * sortedArr[1])
    }else{
        console.log(sortedArr[sortedArr.length - 1] * sortedArr[sortedArr.length - 2])
    }
}

function test3(arr){
    let max, secondMax;
    let min, secondMin;
    if(arr[0]>arr[1]){
        max = arr[0];
        secondMax = arr[1];
        min = arr[1];
        secondMin = arr[0]
    }else{
        max = arr[1];
        secondMax = arr[0];
        min = arr[0];
        secondMin = arr[1]
    }
    for (let i=0 ; i<arr.length ; i++){
        if(arr[i] > max){
            secondMax = max;
            max = arr[i]
        }else if(arr[i] > secondMax){
            secondMax = arr[i];
        }
    }
}
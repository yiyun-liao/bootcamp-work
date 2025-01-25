//[-5, 4, 8, 3, -10]
// 假設資料量是 n
// 3*n^2+1
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
    console.log(max);
}

//n*logn+2
function test2(arr){
    let sortedArr = arr.sort((a,b)=> (a-b)); //1
    if(sortedArr[0] * sortedArr[1] > sortedArr[sortedArr.length - 1] * sortedArr[sortedArr.length - 2]){ //1
        console.log(sortedArr[0] * sortedArr[1]) //1
    }else{
        console.log(sortedArr[sortedArr.length - 1] * sortedArr[sortedArr.length - 2])//1
    }
}

// 3*n+9
function test3(arr){
    let max, secondMax; //1
    let min, secondMin; //1
    if(arr[0]>arr[1]){ //1
        max = arr[0]; //1
        secondMax = arr[1]; //1
        min = arr[1]; //1
        secondMin = arr[0] //1
    }else{
        max = arr[1]; //1
        secondMax = arr[0]; //1
        min = arr[0]; //1
        secondMin = arr[1] //1
    }
    for (let i=2 ; i<arr.length ; i++){ //n
        if(arr[i] > max){ //1
            secondMax = max; //1
            max = arr[i] //1
        }else if(arr[i] > secondMax){
            secondMax = arr[i];
        }
        if(arr[i] < min){ //1
            secondMin = max; //1
            min = arr[i]; //1
        }else if(arr[i] < secondMin ){
            secondMin = arr[i];
        }
    }
    if(min*secondMin > max*secondMax){  //1
        console.log(min*secondMin);  //1
    }else{
        console.log(max*secondMax);
    }
}
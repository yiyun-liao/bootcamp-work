const mainPageAside = document.getElementById('main-page-aside');

document.getElementById('open-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'block';
});

document.getElementById('close-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'none';
});


//week3 add api
//function01 use sync/await
let currentIndex = 10; // 初始化目前的索引
let spotsData = []; // 用來存放 API 的資料

window.addEventListener('resize', checkGridColumn); // 新增只要畫面尺寸不同就改變，不需要整頁 refresh

document.addEventListener('DOMContentLoaded', () => {
    fetchData();
    document.getElementById('load-more').addEventListener('click', () => {
        loadMore();
        checkGridColumn();
    });
});

async function fetchData() {
    try {
        const response = await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
        if (!response.ok) {
            throw new Error("Could not fetch resource");
        }
        const data = await response.json();
        console.log('from api', data);
        spotsData = data.data.results; 
        renderSpots();
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function renderSpots() {
    console.log('show spots', spotsData)
    const smallBoxes = document.querySelectorAll('.small-boxes li');
    console.log('smallBoxes', smallBoxes)
    
    // 更新小框內容 (前三筆資料)
    smallBoxes.forEach((box, index) => {
        if (index < spotsData.length) {
            const spot = spotsData[index];
            const img = box.querySelector('img');
            const p = box.querySelector('p');
            
            const firstImgUrl = spot.filelist.split("http").filter(Boolean).map(url => "http" + url);
            // console.log(firstImgUrl)
            const firstImg = firstImgUrl[0];
            
            img.src = firstImg;
            img.alt = spot.stitle;
            p.textContent = spot.stitle;
        }
    });

    // 更新大框內容 (後十筆資料)
    const bigBoxesLi = document.querySelectorAll('.big-boxes li');

    bigBoxesLi.forEach((box, index) => { 
        if (index < spotsData.length - 3) {
            const spot = spotsData[index + 3];
            const p = box.querySelector('p');

            const firstImgUrl = spot.filelist.split("http").filter(Boolean).map(url => "http" + url);
            const firstImg = firstImgUrl[0];

            box.style.backgroundImage = `url("${firstImg}")`;//forEach 所選到的 box 就是 #big.boxes li
            p.textContent = spot.stitle;
        }
    });

    checkGridColumn();
}

function renderBigBoxes(){
    const bigBoxes = document.querySelector('.big-boxes');
    const templateLi = bigBoxes.querySelector('li');
    const maxToRender = Math.min(currentIndex, spotsData.length); // 確保不超出資料數量

    for (let i = currentIndex - 10; i < maxToRender; i++) {
        const spot = spotsData[i + 3];

        const firstImgUrl = spot.filelist.split("http").filter(Boolean).map(url => "http" + url);
        const firstImg = firstImgUrl[0];

        const newLi = templateLi.cloneNode(true); // 複製模板
        newLi.style.backgroundImage = `url("${firstImg}")`; 
        const newLiP = newLi.querySelector('p');
        newLiP.textContent = spot.stitle; 

        bigBoxes.appendChild(newLi); 
    }
}

function loadMore() {
    if (currentIndex < spotsData.length) {
        currentIndex += 10; // 增加索引
        renderBigBoxes(); // 繼續渲染新的大圖
    } else {
        alert('沒有更多的資料可以載入！');
    }
}


// 用 DOM 做 gallery 不同的尺寸匡，原本只有判斷 (min-width: 600px) and (max-width: 1200px) 
// 現在全部用 DOM 判斷

function checkGridColumn(){
    const bigBoxes = document.querySelectorAll('.big-boxes li');
    if(window.matchMedia("(min-width: 600px) and (max-width: 1200px)").matches){
        bigBoxes.forEach(box => {
            box.style.gridColumn = 'span 1';
        });
        if(currentIndex % 4 !== 0){
            bigBoxes[currentIndex-1].style.gridColumn = 'span 2';
            bigBoxes[currentIndex-2].style.gridColumn = 'span 2';
        }
    }
    else if(window.matchMedia("(max-width: 600px)").matches){
        bigBoxes.forEach(box => {
            box.style.gridColumn = 'span 1';
        });
    } else {
        bigBoxes.forEach((box, index) => {
            if((index + 1) % 5 == 1){
                box.style.gridColumn = 'span 2';
            } else {
                box.style.gridColumn = 'span 1'; 
            }
        });
    }
}




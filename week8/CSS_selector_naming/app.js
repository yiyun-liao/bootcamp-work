const mainPageAside = document.getElementById('main-page-aside');

document.getElementById('open-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'block';
});

document.getElementById('close-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'none';
});

//week3 add api
//function01 use sync/await
document.addEventListener('DOMContentLoaded', () => {
    fetchData();
});

async function fetchData() {
    try {
        const response = await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
        if (!response.ok) {
            throw new Error("Could not fetch resource");
        }
        const data = await response.json();
        console.log(data);
        const spots = data.data.results; 
        renderSpots(spots);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function renderSpots(spots) {
    console.log('show spots', spots)
    const smallBoxes = document.querySelectorAll('.small-boxes li');
    console.log(smallBoxes)
    const bigBoxes = document.querySelectorAll('.big-boxes li');

    // 更新小框內容 (前三筆資料)
    smallBoxes.forEach((box, index) => {
        if (index < spots.length) {
            const spot = spots[index];
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
    bigBoxes.forEach((box, index) => { 
        if (index < spots.length - 3) {
            const spot = spots[index + 3];
            const p = box.querySelector('p');

            const firstImgUrl = spot.filelist.split("http").filter(Boolean).map(url => "http" + url);
            const firstImg = firstImgUrl[0];

            box.style.backgroundImage = `url("${firstImg}")`;//forEach 所選到的 box 就是 #big.boxes li
            p.textContent = spot.stitle;
        }
    });
}




const smallBoxes = document.querySelectorAll('.small-boxes li');
const bigBoxes = document.querySelectorAll('.big-boxes li');
function renderSmall(){
    smallBoxes.forEach((box) => {
        const img = box.querySelector('img');
        const p = box.querySelector('p');
        
        img.src = "/week8/async_and_defer/img/gallery-sample.jpg";
        p.textContent = "";
    });
}
function renderBig(){
    bigBoxes.forEach((box) => {
        const p = box.querySelector('p');
        
        box.style.backgroundImage = "url('/week8/async_and_defer/img/gallery-sample.jpg')";
        p.textContent = "";
    });
}

function init(){
    renderSmall();
    renderBig();
    console.log("defer-script.js 執行！")
}

init();

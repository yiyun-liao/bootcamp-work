const mainPageAside = document.getElementById('main-page-aside');

document.getElementById('open-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'block';
});

document.getElementById('close-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'none';
});


const mainPageAside = document.getElementById('main-page-aside');

document.getElementById('open-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'block';
});

document.getElementById('close-aside').addEventListener('click',function(){
    mainPageAside.style.display = 'none';
});

fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
    console.log(myJson);
  });
//這邊舉例拿了 pokemon api
//https://www.youtube.com/watch?v=37vxWr0WgQk
fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))

//改進的 .then 語法，檢查 response.ok
fetch("https://pokeapi.co/api/v2/pokemon/spongebob") //some wrong api
    .then( response => {
        if(!response.ok){
            throw new Error("Could not fetch resource");
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.log(error))

// async/await
fetchData();
async function fetchData(){
    try{
        // get template string in <input>
        const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
        // fetch api
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`) // 原本寫死 fetch("https://pokeapi.co/api/v2/pokemon/typhlosion")
        if(!response.ok){
            throw new Error("Could not fetch resource");
        }
        const data = await response.json();
        //console.log(data);
        //get img in api
        const pokemonSprite = data.sprites.front_default;
        const imgElement = document.getElementById("pokemonSprite");
        //adjust the html and css
        imgElement.src = pokemonSprite;
        imgElement.style.display = "Block";
    }
    catch(error){
        console.error(error);
    }
}

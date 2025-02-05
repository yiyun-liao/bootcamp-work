document.addEventListener('DOMContentLoaded', function(){
    const form = document.querySelector('form');
    const checkbox = document.getElementById('agree-policy');

    form.addEventListener('submit',async function(event){
        console.log("Submit button clicked");
        if(!checkbox.checked){
            event.preventDefault();
            alert('Please check the checkbox first');
            console.log("Checkbox is not checked! Form submission prevented.");
        }
        event.preventDefault();
        await signin();
    });
})

async function signin(){
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try{
        const response = await fetch("/signin",{
            method:"POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({username, password})
        });
        if(!response.ok){
            throw new Error("HTTP error! Status: ${response.status}")
        }
        const data = await response.json();
        console.log(data)
    }catch(error){
        console.error("Error", error);
    }
}


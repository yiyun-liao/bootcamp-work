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

// 使用表單格式
async function signin(){
    const formData = new FormData();
    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);

    try {
        const response = await fetch("/signin", {
            method: "POST",
            body: formData, // 改用 FormData 來匹配後端的 Form 格式
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error("Error", error);
    }
}

// 使用 JSON 格式
// async function signin(){
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;

//     try{
//         const response = await fetch("/signin",{
//             method:"POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({username, password})
//         });
//         if(!response.ok){
//             throw new Error("HTTP error! Status: ${response.status}")
//         }
//         const data = await response.json();
//         console.log(data)
//     }catch(error){
//         console.error("Error", error);
//     }
// }


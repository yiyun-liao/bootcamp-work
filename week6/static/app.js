document.addEventListener('DOMContentLoaded', function(){
    // const form = document.querySelector('form');
    // const checkbox = document.getElementById('agree-policy');

    // form.addEventListener('submit',async function(event){
    //     console.log("Submit button clicked");
    //     if(!checkbox.checked){
    //         event.preventDefault();
    //         alert('Please check the checkbox first');
    //         console.log("Checkbox is not checked! Form submission prevented.");
    //     }
    //     // event.preventDefault();
    //     // await signin();
    // });
})

document.addEventListener('DOMContentLoaded', function(){
    // signup
    const form = document.getElementById('signup_form')
    const name = document.getElementById('signup_name');
    const username = document.getElementById('signup_username');
    const password = document.getElementById('signup_password');
    const submit = document.getElementById('signup_submit');

    const nameError = document.getElementById('signup_name_error');
    const usernameError = document.getElementById('signup_username_error');
    const passwordError = document.getElementById('signup_password_error');  
    
    function validateSignupInputs(){
        nameError.textContent= name.value === "" ? "姓名不得空白" : "";
        usernameError.textContent= username.value === "" ? "帳號不得空白" : "";
        passwordError.textContent= password.value === "" ? "密碼不得空白" : "";
        submit.disabled = name.value === "" || username.value === "" || password.value === "";
    }

    form.addEventListener('input', validateSignupInputs);
    // name.addEventListener('input',validateSignupInputs);
    // username.addEventListener('input',validateSignupInputs);
    // password.addEventListener('input',validateSignupInputs);

    //signin
    const signinForm = document.getElementById('signin_form')
    const signinUsername = document.getElementById('signin_username');
    const signinPassword = document.getElementById('signin_password');
    const signinSubmit = document.getElementById('signin_submit');

    const signinUsernameError = document.getElementById('signin_username_error');
    const signinPasswordError = document.getElementById('signin_password_error');  
    
    function validateSigninInputs(){
        signinUsernameError.textContent= signinUsername.value === "" ? "帳號不得空白" : "";
        signinPasswordError.textContent= signinPassword.value === "" ? "密碼不得空白" : "";
        signinSubmit.disabled = signinUsername.value === "" || signinPassword.value === "";
    }

    signinForm.addEventListener('input',validateSigninInputs);
})

// // 使用表單格式
// async function signin(){
//     const formData = new URLSearchParams();
//     formData.append("username", document.getElementById("username").value);
//     formData.append("password", document.getElementById("password").value);
//     // console.log(formData.toString()); //username=test&password=test
//     try {
//         const response = await fetch("/signin", {
//             method: "POST",
//             headers: { "Content-Type": "application/x-www-form-urlencoded" },
//             body: formData.toString(),
//         });       
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//         const data = await response.json(); //{ "redirect": "/member.html" } or { "redirect": "/error.html" }
//         if (data.redirect) {
//             window.location.href = data.redirect;
//         }
//     } catch (error) {
//         console.error("Error", error);
//     }
// }



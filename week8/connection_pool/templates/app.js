document.addEventListener('DOMContentLoaded', function(){
    const path = window.location.pathname;

    if(path === "/"){
        // signup
        const name = document.getElementById('signup_name');
        const username = document.getElementById('signup_username');
        const password = document.getElementById('signup_password');
        const submit = document.getElementById('signup_submit');
    
        const nameError = document.getElementById('signup_name_error');
        const usernameError = document.getElementById('signup_username_error');
        const passwordError = document.getElementById('signup_password_error');  
        
        const inputRule = /^[A-Za-z0-9]{2,}$/;
        function validateSignupInputs(){
            nameError.textContent= name.value === "" ? "姓名不得空白" 
                : (!inputRule.test(name.value) ? "姓名只能包含英數字，且至少 2 個字元" : "");
            usernameError.textContent= username.value === "" ? "帳號不得空白" 
                : (!inputRule.test(username.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            passwordError.textContent= password.value === "" ? "密碼不得空白" 
                : (!inputRule.test(password.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            submit.disabled = !(nameError.textContent === "" && usernameError.textContent === "" && passwordError.textContent === "");
        }
    
        document.getElementById('signup_form').addEventListener('input', validateSignupInputs);
    
        //signin
        const signinUsername = document.getElementById('signin_username');
        const signinPassword = document.getElementById('signin_password');
        const signinSubmit = document.getElementById('signin_submit');
    
        const signinUsernameError = document.getElementById('signin_username_error');
        const signinPasswordError = document.getElementById('signin_password_error');  
        
        function validateSignupInputs(){
            usernameError.textContent= username.value === "" ? "帳號不得空白" 
                : (!inputRule.test(username.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            passwordError.textContent= password.value === "" ? "密碼不得空白" 
                : (!inputRule.test(password.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            submit.disabled = !(nameError.textContent === "" && usernameError.textContent === "" && passwordError.textContent === "");
        }

        function validateSigninInputs(){
            signinUsernameError.textContent= signinUsername.value === "" ? "帳號不得空白" 
                : (!inputRule.test(signinUsername.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            signinPasswordError.textContent= signinPassword.value === "" ? "密碼不得空白" 
                : (!inputRule.test(signinPassword.value) ? "帳號只能包含英數字，且至少 2 個字元" : "");
            signinSubmit.disabled = !(signinUsernameError.textContent === "" && signinPasswordError.textContent === "");
        }
    
        document.getElementById('signin_form').addEventListener('input',validateSigninInputs);
    }
})
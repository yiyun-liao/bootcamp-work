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
        
        function validateSignupInputs(){
            nameError.textContent= name.value === "" ? "姓名不得空白" : "";
            usernameError.textContent= username.value === "" ? "帳號不得空白" : "";
            passwordError.textContent= password.value === "" ? "密碼不得空白" : "";
            submit.disabled = name.value === "" || username.value === "" || password.value === "";
        }
    
        document.getElementById('signup_form').addEventListener('input', validateSignupInputs);
    
        //signin
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
    
        document.getElementById('signin_form').addEventListener('input',validateSigninInputs);
    }
    
    if(path==='/member'){
        // createMessage
        const createMessageContent = document.getElementById('create_message_content');
        const createMessageSubmit = document.getElementById('create_message_submit');
        function createMessage(){
            createMessageSubmit.disabled = createMessageContent.value === "";
        }
        createMessageContent.addEventListener('input',createMessage);

        // deleteMessage
        document.querySelectorAll('.mdi-close').forEach(button => {
            button.addEventListener('click', function(){
                const messageId = this.getAttribute('message-id');
                const messageMemberId = this.getAttribute('message-member-id');
                deleteMessage(messageId, messageMemberId);
            });
        })

        async function deleteMessage(messageId, messageMemberId) {
            console.log(messageId, messageMemberId)
            const isConfirmed = confirm("確定要刪除這則留言嗎？");
            if (!isConfirmed){
                return;
            }
            try{
                const response = await fetch(`/deleteMessage/${messageId}/${messageMemberId}`,{
                    method:'DELETE',
                });
                if (!response.ok) {
                    throw new Error("Could not fetch");
                }
                window.location.reload();
            } catch (error){
                console.error("Error fetching data:", error);
            }
        }

    }
})
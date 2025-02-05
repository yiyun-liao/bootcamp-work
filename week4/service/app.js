document.addEventListener('DOMContentLoaded', function(){
    const form = document.querySelector('form');
    const checkbox = document.getElementById('agree-policy');

    form.addEventListener('submit', function(event){
        console.log("Submit button clicked");
        if(!checkbox.checked){
            event.preventDefault();
            alert('Please check the checkbox first');
            console.log("Checkbox is not checked! Form submission prevented.");
        }
    });
})
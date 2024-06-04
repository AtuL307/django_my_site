
document.getElementById("passwordForm"). addEventListener('submit', function(event){
    // console.dir(event);
    const new_pass = document.querySelector('#new_password').value;
    const confirm_new_pass = document.querySelector('#confirm_new_password').value;
    const message = document.querySelector('#message');

    if (new_pass == confirm_new_pass){
        // message.style.color = 'green';
        // message.textContent = 'Passwords match';
        this.submit();
    }
    else{
        event.preventDefault();

        message.style.color = 'red';
        message.textContent = 'Passwords not match.';
    }
})
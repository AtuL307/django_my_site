document.getElementById('author').addEventListener('submit', function(event){
    
    event.preventDefault()
    const inputs = document.querySelectorAll('#author div input');


    for (let input of inputs) {   
        if (input.value.trim() === '') {
            return false;
        }
    }
    alert("Verification mail is send to your mention email address!!");
})

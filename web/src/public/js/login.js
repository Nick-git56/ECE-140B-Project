// function setFormMessage(formElement, type, message) {
//     const messageElement = formElement.querySelector(".form__message");

//     messageElement.textContent = message;
//     messageElement.classList.remove("form__message--success", "form__message--error");
//     messageElement.classList.add(`form__message--${type}`);
// }

// function setInputError(inputElement, message) {
//     inputElement.classList.add("form__input--error");
//     inputElement.parentElement.querySelector(".form__input-error-message").textContent = message;
// }

// function clearInputError(inputElement) {
//     inputElement.classList.remove("form__input--error");
//     inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
// }

function login(){
    var email = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var comp_id = document.getElementById("comp_id").value;
    // document.getElementById("").innerHTML = "";
    console.log(email, password, comp_id);

    fetch('http://localhost/login_verify', {
    method: 'POST', 
    body: JSON.stringify({
        email:email,
        password:password,
        comp_id:comp_id }),

    headers:{
        "Content-Type":"application/json; charset=UTF-8"
    }
    })
    .then(response => response.json())
    .then(data => { console.log('Success:', data); window.location.replace('/test2'); })
    .catch((error) => { console.error('Error:', error); 
});
}

function create_account(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var comp_id = document.getElementById("comp_id").value;
    // document.getElementById("").innerHTML = "";
    console.log(email, password, comp_id);

    fetch('http://localhost/create_account_process', {
    method: 'POST', 
    body: JSON.stringify({
        email:email,
        password:password,
        comp_id:comp_id }),
    headers:{
        "Content-Type":"application/json; charset=UTF-8"
    }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data); 
        window.location.replace('/'); 
        // ***
        

        // ***
    })
    .catch((error) => { console.error('Error:', error); 
});
}

// document.addEventListener("DOMContentLoaded", () => {
//     const loginForm = document.querySelector("#login");
//     const createAccountForm = document.querySelector("#createAccount");

// document.querySelector("#linkCreateAccount").addEventListener("click", e => {
//     e.preventDefault();
//     loginForm.classList.add("form--hidden");
//     createAccountForm.classList.remove("form--hidden");
// });

// document.querySelector("#linkLogin").addEventListener("click", e => {
//     e.preventDefault();
//     loginForm.classList.remove("form--hidden");
//     createAccountForm.classList.add("form--hidden");
// });

// createAccountForm.addEventListener("submit", e => {
//     e.preventDefault();

//     // Perform your AJAX/Fetch login
//     // take form inputs
//     var input = document.getElementById("createAccount").value;
//     // document.getElementById("").innerHTML = "";
//     console.log(input);
//     const data = {input};
    
//     fetch('http://localhost/create_account', {
//     method: 'POST', 
//     headers: {
//         'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data),
//     })
//     .then(response => response.json())
//     .then(data => {
//     console.log('Success:', data);
//     window.location = 'http://localhost/home'
//     })
//     .catch((error) => {
//     console.error('Error:', error);

//     });
   
// });

// loginForm.addEventListener("submit", e => {
//     e.preventDefault();

//     // Perform your AJAX/Fetch login
//     var input = document.getElementById("login").value;
//     // document.getElementById("").innerHTML = "";
//     console.log(input);
//     const data = { input };

//     fetch('http://localhost/login_verify', {
//     method: 'POST', 
//     headers: {
//         'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data),
//     })
//     .then(response => response.json())
//     .then(data => {
//     console.log('Success:', data); 
//     window.location = 'http://localhost/home'
//     })
//     .catch((error) => {
//     console.error('Error:', error);
//     setFormMessage(loginForm, "error", "Invalid username/password combination");
//     });
//     // setFormMessage(loginForm, "error", "Invalid username/password combination");
// });

// document.querySelectorAll(".form__input").forEach(inputElement => {
//     inputElement.addEventListener("blur", e => {
//         if (e.target.id === "signupUsername" && e.target.value.length > 0 && e.target.value.length < 10) {
//             setInputError(inputElement, "Username must be at least 10 characters in length");
//         }
//     });
//     // inputElement.addEventListener("blur", e =>{
//     //     if (e.target.id == "conf_password"){
//     //         const pass1 = document.getElementById("password").value;
//     //         const pass2 = document.getElementById("password").value;
//     //         if (pass1 != pass2){
//     //             setInputError(inputElement_password, "Password don not match.");
//     //         }
//     //     }
//     // });
//     inputElement.addEventListener("input", e => {
//         clearInputError(inputElement);
//     });
// });
// });

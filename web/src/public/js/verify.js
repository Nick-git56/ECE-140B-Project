function load_home() {
    document.getElementById("content").innerHTML='<object type="text/html" data="home.html" ></object>';
}

function login(){
    var email = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var comp_id = document.getElementById("comp_id").value;
    // document.getElementById("").innerHTML = "";
    console.log(email, password, comp_id);

    let URL = '/login_verify';
    fetch(URL)
        .then(response=>response.json())
        .then(function(response) {
            // response ...
            // <p id="locSavedState"></p>
            // let locSavedVal = document.getElementById('locSavedState');
            // locSavedVal.innerHTML = "Location is saved!";
            if(response['verified'] == 'True') {
                // enter dashboard
                console.log('success');
                window.location.href = '/dashboard';
            }
            else{
                // show error
                console.log('failed');
            }
        });

//     fetch('http://localhost/login_verify', {
//     method: 'POST', 
//     body: JSON.stringify({
//         email:email,
//         password:password,
//         comp_id:comp_id }),

//     headers:{
//         "Content-Type":"application/json; charset=UTF-8"
//     }
//     })
//     .then(response => response.json())
//     .then(data => { console.log('Success:', data); window.location.replace('http://localhost/Dashboard'); })
//     .catch((error) => { console.error('Error:', error); 
// });
}

function create_account(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var comp_id = document.getElementById("comp_id").value;
    // document.getElementById("").innerHTML = "";
    console.log(email, password, comp_id);

//     fetch('http://localhost/create_account_process', {
//     method: 'POST', 
//     body: JSON.stringify({
//         email:email,
//         password:password,
//         comp_id:comp_id }),
//     headers:{
//         "Content-Type":"application/json; charset=UTF-8"
//     }
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Success:', data); 
//         window.location.replace('http://localhost/Dashboard'); 
//     })
//     .catch((error) => { console.error('Error:', error); 
// });
}
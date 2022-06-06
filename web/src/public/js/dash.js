var currentTab = 0; // Current tab is set to be the first tab (0)

function openForm() {
  document.getElementById("myForm").style.display = "block";
  showTab(currentTab); // Display the current tab
}

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if(n==0) // I set n==0 until I figure out how to validate only the first form page.
    if (!validateForm()) 
      return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class on the current step:
  x[n].className += " active";
}

function handleSubmit(event) {
    event.preventDefault();

    const data = new FormData(event.target);

    const value = Object.fromEntries(data.entries());

    console.log({ value });
  
  fetch('/create_event', {
    method: 'POST', 
    body: JSON.stringify(value),
    headers:{
        "Content-Type":"application/json; charset=UTF-8"
    }
    })
    .then(response => response.json())
    .then(data => { console.log('Success:', data); window.location.replace('/Dashboard'); })
    .catch((error) => { console.error('Error:', error); 
});
  
  }

  const form = document.querySelector('form');
  form.addEventListener('submit', handleSubmit);

// GET created events from server
async function getEvents() {
    let url = '/get_events';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

// Print created events on dashboard html. 
async function renderEvents() {
    let events = await getEvents();
    let html = 'dashboard';
    events.forEach(event => {
        let htmlSegment = `<div class="values">
                            <div class="header">
                            <h2>${event.ename}</h2>
                            <p>${event.category}</p>
                            </div>
                        </div>`;

        html += htmlSegment;
    });

    let container = document.querySelector('.events-list');
    container.innerHTML = html;
}

renderUsers();


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function servicesItems() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
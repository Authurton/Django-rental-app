// Rating Initialization
$(document).ready(function() {
  $('#rateMe4').mdbRate();
});

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#message').fadeOut('slow');

}, 3000);

// document.querySelector('#comments').style.display = "block";
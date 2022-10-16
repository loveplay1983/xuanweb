/******************** Test **************************/
// jQuery(document).ready(function ($) {
//     alert("js is working");
// });

/********************* datatime in nav ****************************/

// Function to format 1 in 01
const zeroFill = n => {
    return ('0' + n).slice(-2);
}

// Creates interval
const interval = setInterval(() => {
    const now = new Date();
    const day = now.toLocaleDateString('zh-CN', {weekday: "short", year: "numeric"})
    document.getElementById('datetime').innerHTML = day + " " +
        zeroFill(now.getHours()) + ':' +
        zeroFill(now.getMinutes()) + ':' +
        zeroFill(now.getSeconds());
}, 1000);


/*************************************** Query data by pressing the Return Key *********************************/

// Retrieve Patient info
// document.getElementById("patientNum")
//     .addEventListener('keyup', function (event) {
//         if (event.code === 'Enter') {
//             event.preventDefault();
//             alert("The patient data on this page will be removed and the form will commit once!")
//             // document.querySelectorAll("form")[0].reset();
//             document.querySelectorAll("form")[0].submit();
//
//         }
//     });

/********************************* flash message disappear after few sends **************************************/
// window.setTimeout(function() {
//     $(".alert").fadeTo(500, 0)
// }, 4000);


function collectBtn(){
    document.getElementById("data-collect").style.backgroundColor = "red";
}


function clinicBtn(){

}


// patient image slide show
var slideIndex = 1;

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");

    // Reset the index if the current index exceeds the min and max
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }

    // Initialize all the slides to none object
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    // Show up the image with the chosen index
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += "active";
    captionText.innerHTML = dots[slideIndex - 1].alt;
}

showSlides(slideIndex);

function openModal() {
    document.getElementById("myModal").style.display = "block";
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

// print patient list
function printPatient(){
    backAndPrint = document.getElementById("backAndPrint");
    backBtn = document.getElementById("return-index");
    printBtn = document.getElementById("print-list");
    backBtn.remove();
    printBtn.remove();
    window.print();
    backAndPrint.appendChild(backBtn);
    backAndPrint.appendChild(printBtn);
}

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


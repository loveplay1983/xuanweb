/* Datetime display in the navbar */

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


/* Two tabs of the main content */
function openPage(pageName, elmnt, color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

/* Query data without by only pressing the Return key */

// Retrieve Patient info
document.getElementById("patientNum")
    .addEventListener('keyup', function(event) {
        if (event.code === 'Enter')
        {
            event.preventDefault();
            // document.querySelector("form").submit();
            document.querySelectorAll("form")[0].submit();
            // document.getElementById("patientNum").submit();
            // alert("It worked!")
        }
    });


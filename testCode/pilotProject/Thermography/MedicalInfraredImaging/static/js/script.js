/***************************************  Datetime display in the navbar *********************************/

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
/***************************************  Datetime display in the navbar *********************************/


/*************************************** Query data by pressing the Return Key *********************************/

// Retrieve Patient info
document.getElementById("patientNum")
    .addEventListener('keyup', function (event) {
        if (event.code === 'Enter') {
            event.preventDefault();
            alert("It worked!")
            // document.querySelector("form").submit();
            document.querySelectorAll("form")[0].reset();
            document.querySelectorAll("form")[0].submit();
            // document.getElementById("patientNum").submit();

        }
    });
/*************************************** Query data by pressing the Return Key *********************************/

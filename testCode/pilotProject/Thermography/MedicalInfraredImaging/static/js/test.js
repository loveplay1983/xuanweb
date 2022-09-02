var val = document.getElementById("valR").value;
document.getElementById("range").innerHTML = val;
document.getElementById("img").src = '../static/testImage/' + val + ".jpg";

function showVal(newVal) {
    document.getElementById("range").innerHTML = newVal;
    document.getElementById("img").src = '../static/testImage/' + newVal + ".png";
}


// Retrieve Patient info
document.getElementById("patientNum")
    .addEventListener('keyup', function(event) {
        if (event.code === 'Enter')
        {
            event.preventDefault();
            document.getElementById("patientNum").submit();
        }
    });
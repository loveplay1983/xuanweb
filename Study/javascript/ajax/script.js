function loadDoc() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.getElementById("test").innerHTML = this.responseText;
    }

    xhttp.open("GET", "ajax_info.html", true);
    xhttp.send();
}

function rtn() {
    window.location.href = "test.html";
}

/*********js fetch api***********/
let content = "fetchapi_info.html";
fetch(content)
.then(x => x.text())
.then(y => document.getElementById("fetchapi-test").innerHTML = y)
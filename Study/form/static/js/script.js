function mouseCoord() {
    document.addEventListener('mousemove', (event) => {
        const {
            screenX,
            screenY
        } = event
        let result = document.getElementById("screen");
        result.innerHTML = "<b>X-</b>" + screenX + "<br><b>Y-" + screenY;
    })
}

mouseCoord()


var slider = document.getElementById("range");
var currentNum = document.getElementById("targetNum");
currentNum.innerHTML = slider.value;

slider.oninput = function () {
    currentNum.innerHTML = this.value;  // this.value means slider.value
}

function helloworld() {
    var firstName = document.getElementById("name");
    var lname = document.getElementById("name2");
    alert("Welcome, " + firstName.value + " " + lname.value);
}


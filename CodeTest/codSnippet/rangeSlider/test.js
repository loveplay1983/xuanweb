var val = document.getElementById("valR").value;
document.getElementById("range").innerHTML = val;
document.getElementById("img").src = val + ".jpg";

function showVal(newVal) {
    document.getElementById("range").innerHTML = newVal;
    document.getElementById("img").src = newVal + ".png";
}



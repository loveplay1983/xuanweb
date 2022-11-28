let count = 0;   // set the initial value for counter

// select value and buttons
const value = document.querySelector("#value");
const btns = document.querySelectorAll(".btn");

// if condition for increase, decrease and reset value
btns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
        const styles = e.currentTarget.classList;
        if (styles.contains("decrease")) {
            count--;
        } else if (styles.contains("increase")) {
            count++;
        } else {
            count = 0;
        }
        // change button color
        if (count > 0) {
            value.style.color = "green";
        }
        if (count < 0) {
            value.style.color = "red";
        }
        if (count === 0) {
            value.style.color = "#333";
        }
        //display value
        value.textContent = count;
    });
})
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
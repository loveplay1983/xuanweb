// Function to format 1 in 01
const zeroFill = n => {
    return ('0' + n).slice(-2);

    // return ('0' + n);
}

const now = new Date();
const day = new Date().toLocaleDateString('zh-CN', {weekday:"short", year:"numeric"})

// document.getElementById('a').innerHTML = now.getDay();
document.getElementById('a').innerHTML = day + " " + zeroFill(now.getHours()) + ':' +
    zeroFill(now.getMinutes()) + ':' + zeroFill(now.getSeconds());
// new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short", day:"numeric"})


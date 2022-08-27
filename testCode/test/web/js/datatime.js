// Function to format 1 in 01
const zeroFill = n => {
    return ('0' + n).slice(-2);
}

// Creates interval
const interval = setInterval(() => {
    const now = new Date();
    const day = now.toLocaleDateString('zh-CN', {weekday: "short", year: "numeric"})

    // document.getElementById('datetime').innerHTML = day
    document.getElementById('datetime').innerHTML = day + " " +
        zeroFill(now.getHours()) + ':' +
        zeroFill(now.getMinutes()) + ':' +
        zeroFill(now.getSeconds());
    // new Date().toLocaleDateString('en-us', { weekday:"long",
    //     year:"numeric",
    //     month:"short",
    //     day:"numeric"})
}, 1000);


// // Function to format 1 in 01
// const zeroFill = n => {
//     return ('0' + n).slice(-2);
// }
//
// // Creates interval
// const interval = setInterval(() => {
//     // Get current time
//     const now = new Date();
//
//     // Format date as in mm/dd/aaaa hh:ii:ss
//     const dateTime = zeroFill((now.getMonth() + 1)) + '/' +
//         zeroFill(now.getUTCDate()) + '/' + now.getFullYear() +
//         ' ' + zeroFill(now.getHours()) + ':' + zeroFill(now.getMinutes()) +
//         ':' + zeroFill(now.getSeconds());
//
//     // Display the date and time on the screen using div#date-time
//     document.getElementById('date-time').innerHTML = dateTime;
// }, 1000);
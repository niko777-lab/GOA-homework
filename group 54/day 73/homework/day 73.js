let count = 1;
let counterInterval = setInterval(() => {
    console.log(count);
    count++;
    if (count > 5) clearInterval(counterInterval);
}, 1000);

let msgInterval = setInterval(() => {
    console.log("This message appears every 2 seconds");
}, 2000);
setTimeout(() => clearInterval(msgInterval), 10000);

let colors = ["#f8b400", "#6a2c70", "#b83b5e", "#0bceaf", "#f38181"];
let colorIndex = 0;
let colorChangeCount = 0;
let colorInterval = setInterval(() => {
    document.body.style.background = colors[colorIndex % colors.length];
    colorIndex++;
    colorChangeCount++;
    if (colorChangeCount >= 5) clearInterval(colorInterval);
}, 3000);

let h = 14, m = 22, s = 5, timeCount = 0;
let timeInterval = setInterval(() => {
    s++;
    if (s === 60) {
        s = 0;
        m++;
        if (m === 60) {
            m = 0;
            h = (h + 1) % 24;
        }
    }
    let clock =
        (h < 10 ? "0" : "") + h + ":" +
        (m < 10 ? "0" : "") + m + ":" +
        (s < 10 ? "0" : "") + s;
    console.log(clock);
    timeCount++;
    if (timeCount >= 15) clearInterval(timeInterval);
}, 1000);

let timer = 0;
let timerInterval = setInterval(() => {
    timer++;
    console.log("Timer:", timer, "seconds");
    if (timer >= 10) clearInterval(timerInterval);
}, 1000);

let arr1 = [10, 20, 30, 40];
console.log("Second element:", arr1[1]);

arr1[0] = 100;
console.log("Modified array:", arr1);

let arr2 = ["apple", "banana", "cherry"];
console.log(arr2[0]);
console.log(arr2[1]);
console.log(arr2[2]);

let arr3 = [5, 10, 15, 20, 25];
let sum = arr3[0] + arr3[arr3.length - 1];
console.log("Sum of first and last:", sum);

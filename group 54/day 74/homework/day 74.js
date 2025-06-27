function changeText() {
    document.getElementById("para").textContent = "ტექსტი შეიცვალა!";
}

let bgInterval;
let bgIndex = 0;
const bgColors = ["#ffcccc", "#ccffcc", "#ccccff", "#ffffcc", "#ffccff"];
function startBgLoop() {
    if (bgInterval) return;
    bgInterval = setInterval(function() {
        document.body.style.backgroundColor = bgColors[bgIndex];
        bgIndex = (bgIndex + 1) % bgColors.length;
    }, 2000);
}

function addName() {
    const value = document.getElementById("nameInput").value;
    if (value !== "") {
        const li = document.createElement("li");
        li.textContent = value;
        document.getElementById("nameList").appendChild(li);
        document.getElementById("nameInput").value = "";
    }
}

let fakeHour = 14;
let fakeMin = 22;
let fakeSec = 0;
setInterval(function () {
    fakeSec++;
    if (fakeSec === 60) {
        fakeSec = 0;
        fakeMin++;
        if (fakeMin === 60) {
            fakeMin = 0;
            fakeHour = (fakeHour + 1) % 24;
        }
    }

    const formatted =
        (fakeHour < 10 ? "0" : "") + fakeHour + ":" +
        (fakeMin < 10 ? "0" : "") + fakeMin + ":" +
        (fakeSec < 10 ? "0" : "") + fakeSec;

    document.getElementById("clock").textContent = formatted;
}, 1000);

const cycleColors = ["red", "green", "blue", "purple"];
let colorPos = 0;
function cycleColor() {
    document.body.style.backgroundColor = cycleColors[colorPos];
    colorPos = (colorPos + 1) % cycleColors.length;
}

function generateBoxes() {
    const num = parseInt(document.getElementById("boxNum").value);
    const container = document.getElementById("colorBoxes");
    container.innerHTML = "";
    const boxColors = ["#f88", "#8f8", "#88f", "#ff0", "#f0f"];
    for (let i = 0; i < num; i++) {
        const box = document.createElement("div");
        box.style.backgroundColor = boxColors[i % boxColors.length];
        container.appendChild(box);
    }
}

function startCountdown() {
    let time = parseInt(document.getElementById("seconds").value);
    const output = document.getElementById("countdown");
    const timer = setInterval(function() {
        if (time > 0) {
            output.textContent = time;
            time--;
        } else {
            output.textContent = "დრო დასრულდა!";
            clearInterval(timer);
        }
    }, 1000);
}

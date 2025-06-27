document.getElementById("btn1").addEventListener("click", function() {
    const colorCode = document.getElementById("colorInput").value.trim();
    if (colorCode.match(/^#([0-9a-f]{3}|[0-9a-f]{6})$/i)) {
        document.body.style.backgroundColor = colorCode;
    } else {
        alert("გთხოვთ შეიყვანოთ სწორი HEX კოდი, მაგ: #ffcc00");
    }
});

const btn2 = document.getElementById("btn2");
const colorList = ["red", "blue", "green", "purple", "orange"];
let count = 0;
let intervalId = null;

btn2.addEventListener("click", function() {
    if (intervalId) return;
    intervalId = setInterval(() => {
        btn2.style.backgroundColor = colorList[count % colorList.length];
        count++;
        if (count === 5) {
            clearInterval(intervalId);
            intervalId = null;
            count = 0;
        }
    }, 2000);
});

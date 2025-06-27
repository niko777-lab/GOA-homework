const divBlock = document.getElementById("myDiv");
const paragraphs = divBlock.getElementsByTagName("p");

for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.color = "green";
    paragraphs[i].style.backgroundColor = "black";
}

let fontSize = 10;
let intervalStarted = false;

function increaseFontSize() {
    intervalStarted = true;
    setInterval(function () {
        fontSize += 1;
        document.getElementById("myParagraph").style.fontSize = fontSize + "px";
    }, 1000);
}

let position = 0;
let intervalStarted1 = false;

document.getElementById("moveButton").addEventListener("click", function ()  {
    intervalStarted = true;

    setInterval(function () {
    position -= 50;
    document.getElementById("moveButton").style.left = position + "px";
}, 1000);
});
// 2
const pTags = document.getElementsByTagName("p");
alert("Number of <p> tags: " + pTags.length);

// 3
const h2Tags = document.getElementsByTagName("h2");
for (let i = 0; i < h2Tags.length; i++) {
    h2Tags[i].style.color = "blue";
}

// 4
const liTags = document.getElementsByTagName("li");
for (let i = 0; i < liTags.length; i++) {
    console.log(liTags[i].textContent);
}

// 5
const divs = document.getElementsByTagName("div");
for (let i = 0; i < divs.length; i++) {
    divs[i].style.backgroundColor = "lightgray";
}

// 6
const firstImage = document.getElementsByTagName("img")[0];
firstImage.src = "https://via.placeholder.com/200";

// 7
const highlights = document.getElementsByClassName("highlight");
for (let i = 0; i < highlights.length; i++) {
    highlights[i].style.backgroundColor = "yellow";
}

// 8
const cards = document.getElementsByClassName("card");
console.log("Card elements: " + cards.length);

// 9
const errors = document.getElementsByClassName("error");
for (let i = 0; i < errors.length; i++) {
    errors[i].style.color = "red";
}

// 10
const items = document.getElementsByClassName("item");
for (let i = 0; i < items.length; i++) {
    console.log(items[i].innerHTML);
}

// 11
const firstBtn = document.getElementsByClassName("button")[0];
firstBtn.textContent = "Clicked!";

// 12
let box = document.getElementById("box");
let pos = 0;
setInterval(() => {
    pos += 5;
    box.style.left = pos + "px";
}, 100);

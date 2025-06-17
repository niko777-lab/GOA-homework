let p = document.getElementById("Main_p");


p.onclick = function() {
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
    document.body.style.textAlign = "center";
}

function handleClick(e) {
    console.log(e);
    e.target.style.backgroundColor = "black";
}
let button = document.getElementById("myButton");
button.addEventListener("click", handleClick);

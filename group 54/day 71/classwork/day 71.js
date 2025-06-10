// HTML ნაწილი (მაგალითად, index.html-ში ჩასაწერად)
{/* 
<div id="myDiv"></div>
<script src="day 71.js"></script>
*/}

// JS ნაწილი (day 71.js)
function generateParagraph() {
    let div = document.getElementById('myDiv');
    let p = document.createElement('p');
    p.textContent = 'blblalblbls';
    div.appendChild(p);
}

generateParagraph()
function removeChildElement() {
    let parentDiv = document.getElementById("parent"); // parent div
    let childDiv = document.getElementById("child");   // child div

    if (childDiv) {
        parentDiv.removeChild(childDiv); // remove the child element
    }
}
function replaceParagraph() {
    let parentDiv = document.getElementById("parent"); 
    let oldParagraph = document.getElementById("oldParagraph"); 
    let newParagraph = document.createElement("p"); 

    newParagraph.textContent = "This is the new paragraph.";
    
    if (oldParagraph) {
        parentDiv.replaceChild(newParagraph, oldParagraph); 
    }
}
replaceParagraph();
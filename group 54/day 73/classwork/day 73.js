let count = 0;
let interval1 = setInterval(function() {
    console.log("Nikolozi");
    count++;
    if (count === 4) {
        clearInterval(interval1);
    }
}, 5000);

const array = ["hello world!", 42, true, { name: "Nikolozi" }];
console.log(array);
console.log(array[3]);

const array1 = ["hello GOA", 12, false,{ surname: "Iobidze"}]
function printArrayEveryElement(arr) {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
}

printArrayEveryElement(array1);
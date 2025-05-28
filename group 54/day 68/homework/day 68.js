/* 2-5 */

// Check if two numbers are both greater than 10
let a = 15, b = 12;
console.log(a > 10 && b > 10); // true

// Check if at least one of two conditions is true
let x = 5, y = 20;
console.log(x > 10 || y > 10); // true

// Use the NOT operator to invert a boolean value
let isSunny = false;
console.log(!isSunny); // true

// Combine multiple logical operations in a single expression
let num1 = 8, num2 = 15, num3 = 20;
console.log((num1 > 5 && num2 > 10) || num3 < 10); // true

/* 6-10 */

// Convert a number to a string using String()
let number = 123;
let numberStr = String(number);
console.log(numberStr, typeof numberStr); // "123" "string"

// Convert a boolean value to a string using String()
let boolVal = true;
let boolStr = String(boolVal);
console.log(boolStr, typeof boolStr); // "true" "string"

// Convert a string containing a number to a number using Number()
let strNum = "456";
let num = Number(strNum);
console.log(num, typeof num); // 456 "number"

// Use Number() to convert a boolean to a number
console.log(Number(true));  // 1
console.log(Number(false)); // 0

// Check what happens when you use Number() on a non-numeric string
console.log(Number("hello")); // NaN

/* 11) Check if a Number is Positive or Negative */
let userNum = Number(prompt("Enter a number:"));
if (userNum > 0) {
    alert("The number is positive.");
} else if (userNum < 0) {
    alert("The number is negative.");
} else {
    alert("The number is zero.");
}

/* 12) Check User’s Age for Voting Eligibility */
let age = Number(prompt("Enter your age:"));
if (age >= 18) {
    alert("You can vote!");
} else {
    alert("You are not eligible to vote.");
}

/* 13) Compare Two Numbers */
let firstNum = Number(prompt("Enter the first number:"));
let secondNum = Number(prompt("Enter the second number:"));
if (firstNum > secondNum) {
    alert("The first number is larger.");
} else if (firstNum < secondNum) {
    alert("The second number is larger.");
} else {
    alert("Both numbers are equal.");
}
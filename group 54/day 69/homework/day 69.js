/* 2) Even or Odd */
function evenOrOdd(num) {
    if (num % 2 === 0) {
        console.log(num + " is even");
    } else {
        console.log(num + " is odd");
    }
}
// Example: evenOrOdd(7);

/* 3) Assign Grade */
function assignGrade(score) {
    if (score >= 90) {
        console.log("Grade A");
    } else if (score >= 80) {
        console.log("Grade B");
    } else if (score >= 70) {
        console.log("Grade C");
    } else if (score >= 60) {
        console.log("Grade D");
    } else {
        console.log("Fail");
    }
}
// Example: assignGrade(85);

/* 4) Largest Among Three Numbers */
function largestOfThree(a, b, c) {
    if (a === b && b === c) {
        console.log("All numbers are equal");
    } else if (a >= b && a >= c) {
        console.log(a + " is the largest");
    } else if (b >= a && b >= c) {
        console.log(b + " is the largest");
    } else {
        console.log(c + " is the largest");
    }
}
// Example: largestOfThree(5, 9, 3);

/* 5) Vowel or Consonant */
function vowelOrConsonant(char) {
    let vowels = "aeiouAEIOU";
    if (char.length === 1 && ((char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z'))) {
        if (vowels.includes(char)) {
            console.log(char + " is a vowel");
        } else {
            console.log(char + " is a consonant");
        }
    } else {
        console.log("Invalid input");
    }
}
// Example: vowelOrConsonant('e');

/* 6) Divisible by 3 and 5 */
function divisibleBy3And5(num) {
    if (num % 3 === 0 && num % 5 === 0) {
        console.log("Divisible by both");
    } else if (num % 3 === 0) {
        console.log("Divisible by 3 only");
    } else if (num % 5 === 0) {
        console.log("Divisible by 5 only");
    } else {
        console.log("Not divisible by either");
    }
}
// Example: divisibleBy3And5(15);

/* 7) Age Category */
function ageCategory(age) {
    if (age >= 0 && age <= 12) {
        console.log("Child");
    } else if (age >= 13 && age <= 19) {
        console.log("Teenager");
    } else if (age >= 20 && age <= 59) {
        console.log("Adult");
    } else if (age >= 60) {
        console.log("Senior");
    } else {
        console.log("Invalid age");
    }
}
// Example: ageCategory(25);

/* 8) Print numbers from 1 to 5 (while loop) */
let i = 1;
while (i <= 5) {
    console.log(i);
    i++;
}

/* 9) Print even numbers from 2 to 10 (while loop) */
let j = 2;
while (j <= 10) {
    console.log(j);
    j += 2;
}

/* 10) Print numbers from 10 down to 1 (while loop) */
let k = 10;
while (k >= 1) {
    console.log(k);
    k--;
}

/* 11) Print numbers from 1 to 10 (for loop) */
for (let m = 1; m <= 10; m++) {
    console.log(m);
}

/* 12) Print first 5 multiples of 3 (for loop) */
for (let n = 1; n <= 5; n++) {
    console.log(n * 3);
}

/* 13) Print numbers from 10 to 1 in reverse (for loop) */
for (let p = 10; p >= 1; p--) {
    console.log(p);
}

/* 14) Print all even numbers between 1 and 20 (for loop) */
for (let q = 1; q <= 20; q++) {
    if (q % 2 === 0) {
        console.log(q);
    }
}

/* 15) Print the sum of numbers from 1 to 5 (for loop) */
let sum = 0;
for (let r = 1; r <= 5; r++) {
    sum += r;
}
console.log("Sum:", sum);
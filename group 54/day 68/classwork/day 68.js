function logicalFunc(bool1, bool2) {
    console.log("AND (&&) result:", bool1 && bool2);
    console.log("OR (||) result:", bool1 || bool2);
}

// პირველი გამოძახება
logicalFunc(true, false);

// მეორე გამოძახება
logicalFunc(false, false);

// მესამე გამოძახება
logicalFunc(true, true);

function typeConvert() {
    let input = prompt("შეიყვანეთ რიცხვი:");
    console.log("შეყვანილი მნიშვნელობა:", input);
    let numberValue = Number(input);
    console.log("რიცხვად გარდაქმნილი მნიშვნელობა:", numberValue);
    console.log("მონაცემთა ტიპი:", typeof numberValue);
}

typeConvert();

// საკლასო დავალება:

// შეცვალეთ მოცემული კოდი ისე, რომ ასაკებზე გამოქონდეს შემდეგი წინადადებები:

// 0-18 - not adult
// 18-65 - adult & not old
// 65-113 - retired
// 113+ - lie


function forConditions() {
    let userNum = Number(prompt("Enter age:"));

    if (userNum >= 0 && userNum < 18) {
        console.log("not adult");
    } else if (userNum >= 18 && userNum < 65) {
        console.log("adult & not old");
    } else if (userNum >= 65 && userNum <= 113) {
        console.log("retired");
    } else if (userNum > 113) {
        console.log("lie");
    } else {
        console.log("Invalid input");
    }
}
forConditions();

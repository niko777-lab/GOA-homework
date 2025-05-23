function concStrings() {
    let str1 = prompt("შეიყვანეთ პირველი სტრინგი:");
    let str2 = prompt("შეიყვანეთ მეორე სტრინგი:");
    console.log(str1 + str2);
}
// საკლასო დავალება:

// შექმენით ფუნქცია სახელად compareStrings. ამ ფუნქციაში შექმენით ორი ცვლადი და ორივეში შეინახეთ მომხმარებლის მიერ prompt-ში შემოტანილი ინფორმაცია. დაბეჭდეთ კონსოლში მკაცრი და არამკაცრი ტოლობების შედარებები.

// ეს ფუნქცია გამოიძახეთ მაშინ, როდესაც ვებსაიტი ჩაიტვირთება
function compareStrings() {
    let str1 = prompt("Enter first string mister!:");
    let str2 = prompt("Enter secoend string mister!:");

    console.log(str1 === str2); // მკაცრი ტოლობა
    console.log(str1 == str2);  // არამკაცრი ტოლობა
}
// საკლასო დავალება:

// შექმენით ფუნქცია სახელად compareNums, რომელსაც ექნება 2 პარამეტრი - num1, num2. ფუნქციამ უნდა აწარმოოს შემდეგი შედარების ოპერაციები ამ რიცხვებზე: >, >=, <, <=, ==, ===, !=, !==.

// ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით
compareStrings();
function compareNums(num1, num2) {
    console.log(num1 > num2);   // მეტია
    console.log(num1 >= num2);  // მეტია ან ტოლი
    console.log(num1 < num2);   // ნაკლებია
    console.log(num1 <= num2);  // ნაკლებია ან ტოლი
    console.log(num1 == num2);  // ტოლი
    console.log(num1 === num2); // მკაცრი ტოლობა
    console.log(num1 != num2);  // არ უდრის
    console.log(num1 !== num2); // მკაცრი ტოლობა არ უდრის
}
compareNums(5, 10);
compareNums(10, 5);
compareNums(5, 5);
// // <!-- საკლასო დავალება:

// შექმენით ფორმა, რომელსაც გაუწერთ id-ის. მას გადაეცით 3 ინფუთი, თითოეულ ინფუთს უნდა ჰქონდეს type, name, required, placeholder ატრიბუტები გაწერილი. ბოლოს ფორმაში ჩაამატეთ დადასტურების ღილაკი.

// როდესაც ფორმა დადასტურდება უნდა გაეშვას ფუნქცია, რომელიც ჯერ წამოიღებს ფორმას, ხოლო შემდეგ მისი ინფუთების მნიშვნელობებს name კუთვნილების გამოყენებით.

// ფუნქციის გამოძახება ისე გაწერეთ, რომ ვებსაიტი არ დარეფრეშდეს ფორმის დადასტურებისას -->
function handleSubmit(e){
    e.preventdefault(); // Prevent the default form submission behavior
    let form = document.getElementById('myForm'); // Get the form by its ID

    let name = form.elements.name.value;
    let surname = form.elements.surname.value;
    let email = form.elements.email.value;
    console.log(name)
    console.log(surname);
    console.log(email);
}

let my_info = {
    name: "nikolozi",
    surname: "iobidze",
    academy: "GOA",
    role: "student",
    city: "tbilisi",
    favColor: "orange",
    favLanguage: "javascript",
    greet() {
        console.log("Hello");
    },
    printProperty(prop) {
        console.log(this[prop]);
    }
};

// 1. დაბეჭდეთ მთლიანი ობიექტი.
console.log(my_info);

// 2. დაბეჭდეთ ობიექტის რომელიმე კუთვნილების მნიშვნელობა.
console.log(my_info.academy);

// 3. ობიექტის რომელიმე კუთვნილებას შეუცვალეთ მნიშვნელობა და დაბეჭდეთ განახლებული მნიშვნელობა.
my_info.city = "batumi";
console.log(my_info.city);

// 4. გამოიძახეთ ობიექტის რომელიმე მეთოდი
my_info.greet();
my_info.printProperty("favColor");
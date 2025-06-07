function usingWhileLoop() {
    let i = 0;
    while (i < 100) {
        console.log(i);
        i++;
    }
}

// usingWhileLoop()
// საკლასო დავალება:

// შექმენით ფუნქცია, სახელად correctUserPassword. ამ ფუნქციაში აიღეთ ერთი ცვლადი, სადაც შეინახავთ სწორ პაროლს. შემდეგ მომხმარებელს შემოატანინეთ თავისი პაროლი. სანამ მომხმარებლის შემოტანილი პაროლი არ იქნება სწორი, თავიდან შემოატანინეთ. 
// ბოლოს, დაუბეჭდეთ correct guess და ასევე დაუწერეთ რამდენი ცდა დასჭირდა.
// ფუნქცია გაუშვით მაშინ, როდესაც ვებსაიტი ჩაიტვირთება
function correctUserPassword() {
    let correct_pass= "12345";
    let password = prompt("შეიყვანე პაროლი:"); 
    let count = 1; 
    while (password !== correct_pass) {
        password = prompt("არასწორია! სცადე თავიდან:");
        count++;
    }

    alert("correct guess! რამდენი ცდა დაგჭირდა: " + count);
}


correctUserPassword()

for (let i = 0; i < 10; i++) {
    console.log("Nikoloz iobidze");
}
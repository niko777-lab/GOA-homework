# # მომხმარებლისგან მთელი რიცხვის შემოტანა
user_number = int(input("შეიყვანეთ მთელი რიცხვი: "))

# პირობითი განცხადება
if user_number > 0:
    print("Bigger than 0")
elif user_number == 0:
    print("0")
else:
    print("smaller than 0")

# მომხმარებლისგან ორი მთელი რიცხვის შემოტანა
num1 = int(input("შეიტანეთ პირველი მთელი რიცხვი: "))
num2 = int(input("შეიტანეთ მეორე მთელი რიცხვი: "))

# დიაპაზონის შექმნა და ბეჭდვა
if num1 > num2:
    for i in range(num2, num1 + 1):
        print(i)
elif num2 > num1:
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("numbers are equal")  

# მომხმარებლისგან ქულის შემოტანა
score = int(input("შეიტანეთ ქულა (0-100): "))

# ნიშნის განსაზღვრა
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"

# ნიშნის დაბეჭდვა
print("Your grade is:", grade)





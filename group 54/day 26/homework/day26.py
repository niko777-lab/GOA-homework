# # 2) თქვენი სიტყვებით ახსენით რა არის elif და როდის ვიყენებთ მას 
# # elif არის თითქმის იგივე როგორც else მაგარამ eelif აქვს blok რომელზეც უნდა იმიუშაოს და else არ აქვს პირობა

# # მომხმარებლისგან სამი რიცხვის შეყვანა
# num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
# num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
# num3 = float(input("შეიყვანეთ მესამე რიცხვი: "))

# # ყველაზე დიდი რიცხვის პოვნა
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3

# # ყველაზე დიდი რიცხვის დაბეჭდვა
# print("ყველაზე დიდი რიცხვი არის:", largest)

# # პაროლის შეყვანა და არასწორი პაროლების რაოდენობის ინიციალიზაცია
# correct_password = "Goa best"
# attempts = 0
# password = ""

# # while ციკლი, რომელიც ითხოვს პაროლის შეყვანას
# while password != correct_password:
#     password = input("შეიყვანეთ პაროლი: ")
#     if password != correct_password:
#         attempts += 1
#         print("პაროლი არასწორია. სცადეთ კიდევ ერთხელ.")

# # არასწორი პაროლების რაოდენობის დაბეჭდვა
# print("არასწორი პაროლების რაოდენობა არის:", attempts)


# მომხმარებლისგან ორი რიცხვის და ოპერატორის შეყვანა
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operator = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")

# გამოთვლის შესრულება და შედეგის ჩვენება
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "გამყოფი არ შეიძლება იყოს ნული"
else:
    result = "არასწორი ოპერატორი"

print("შედეგი არის:", result)


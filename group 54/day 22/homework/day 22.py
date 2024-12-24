# 1) თქვენი სიტყვებით ახსენით განსხვავება while და for ციკლებს შორის
# while მაშილ ვიყენებთ როცა არ ვიცით რამდენი იტერაცია და for მაშინ როდესაც ვიცით რამდენი იტერაცია გვაქ
# 2) დაბეჭდეთ "GOA BEST!!!" 50-ჯერ, ორივე ციკლით შეასრულეთ ეს დავალება
for i in range(50):
    print("GOA BEST!!!")

count = 0
while count < 50:
    print("GOA BEST!!!")
    count += 1

count = 1
while count > 10:
    print(count)
    count += 1

number = 2
while number != 22:
    print(number)
    number += 2

count = 10
while count != 0:
    print(count)
    count = count - 1
print("Blast off!")

count = 1
while count != 11:
    print(count)
    count = count + 1
# 2) დაბეჭდე შენი სახელი
print("ნიკოლოზ იობიძე")  #  ჩაწერ შენს სახელს

# 3) დაბეჭდე საყვარელი ციტატა (ბრჭყალებით)
print('"წარმატება მოდის მათთან, ვინც არ ნებდება."')

# 4) დაბეჭდე რამდენიმე ხაზი (სამსტრიქონიანი შეტყობინება)
print("ვარდები წითელია,")
print("იები ლურჯია,")
print("პითონი მაგარია და ასევე არის GOA")

# 5) დაბეჭდე მარტივი მათემატიკური შედეგი
print(2 + 3)  # დაბეჭდავს: 5

# 6) დაბეჭდე მარტივი ფიგურა სიმბოლოებით (სამკუთხედი)
print("  *  ")
print(" *** ")
print("*****")
# 7) სტრინგის კონვერტირება მთლიან რიცხვად
# დავქონვერტიროთ სტრინგი "42" მთლიან რიცხვად და დავბეჭდოთ
num_str = "42"
num_int = int(num_str)
print(num_int)  # დაბეჭდავს: 42

# 8) ორი ათწილადი რიცხვის შეკრება
# შევქმნათ ორი float ტიპის ცვლადი და შევკრიბოთ
a = 3.5
b = 2.5
print(a + b)  # დაბეჭდავს: 6.0

# 9) ორი სტრინგის შეერთება
# მაგალითად: "Hello" და "World"
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # დაბეჭდავს: Hello World

# 10) მონაცემთა ტიპების დაბეჭდვა
# შევქმნათ int, str და float ტიპის ცვლადები და დავბეჭდოთ მათი ტიპი
x = 10         # int
y = "Python"   # str
z = 3.14       # float

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

# 11) მომხმარებლის ასაკის შეტანა და მომდევნო წლის გამოთვლა
# input() იღებს სტრინგს, ამიტომ ვქცევთ int ტიპად
age = int(input("შენი ასაკი რამდენია? "))
next_year = age + 1
print("შენ მომავალ წელს იქნები", next_year, "წლის")
# 12) ჰკითხე მომხმარებელს სახელი და მიესალმე
name = input("რა გქვია? ")
print("გამარჯობა, " + name + "!")

# 13) ჰკითხე ასაკი და გამოთვალე რამდენის იქნება მომავალ წელს
age = int(input("რამდენი წლის ხარ? "))
print("მომავალ წელს იქნები", age + 1, "წლის.")

# 14) მარტივი კალკულატორი - შეკრება
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print("შედეგი:", num1 + num2)

# 15) საყვარელი ფერი
color = input("შენი საყვარელი ფერი რომელია? ")
print("შენი საყვარელი ფერია", color + "!")

# 16) სიმაღლის შემოწმება
height = int(input("რა არის შენი სიმაღლე სანტიმეტრებში? "))
if height > 150:
    print("შენ მაღალი ხარ!")
else:
    print("შენ 150 სმ-ზე დაბალი ხარ.")
# 17) დაბეჭდე რიცხვები 1-დან 5-მდე
for i in range(1, 6):
    print(i)

# 18) დაბეჭდე სტრინგის თითოეული ასო ახალ ხაზზე
text = "Python"
for i in text:
    print(i)

# 19) რიცხვების 1-დან 10-მდე ჯამის გამოთვლა
total = 0
for i in range(1, 11):
    total += i
print("ჯამი არის:", total)

# 20) გამრავლების ტაბულა 2-ზე (2x1, 2x2, ..., 2x5)
for i in range(1, 6):
    print("2 x", i, "=", 2 * i)

# 21) დაბეჭდე ყველა ლუწი რიცხვი 2-დან 20-მდე
for i in range(2, 21, 2):
    print(i)
# 22) დაბეჭდე რიცხვები 1-დან 5-მდე while loop-ით
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) 1-დან 5-მდე რიცხვების ჯამი while loop-ით
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("ჯამი არის:", total)

# 24) დაითვალე 10-დან 1-მდე უკუთვლით
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) დაბეჭდე ყველა კენტი რიცხვი 1-დან 10-მდე
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) სთხოვე მომხმარებელს შეიყვანოს რაღაც სანამ არ დაწერს "exit"
user_input = ""
while user_input != "exit":
    user_input = input("შეიყვანე ტექსტი (ან დაწერე 'exit' გასასვლელად): ")
# 27) დაბეჭდე სიის ყველა ელემენტი
fruits = ["ვაშლი", "ბანანი", "სტაფილო"]
for item in fruits:
    print(item)

# 28) იპოვე სიის სიგრძე
numbers = [4, 7, 2, 9, 5]
print("ელემენტების რაოდენობა სიაში არის:", len(numbers))

# 29) წვდომა კონკრეტულ ელემენტზე (მეორე ელემენტი — ინდექსი 1)
nums = [10, 20, 30, 40]
print("მეორე ელემენტია:", nums[1])  # დაბეჭდავს: 20

# 30) ელემენტის დამატება სიაში
colors = ["წითელი", "ლურჯი", "მწვანე"]
colors.append("ყვითელი")
print("განახლებული სია:", colors)

# 31) ელემენტის წაშლა სიიდან
animals = ["კატა", "ძაღლი", "ზღარბი"]
animals.remove("ძაღლი")
print("სია წაშლის შემდეგ:", animals)
# 32) შექმენი რიცხვების კვადრატების სია 1-დან 5-მდე
squares = [x**2 for x in range(1, 6)]
print("კვადრატები:", squares)  # [1, 4, 9, 16, 25]

# 33) ლუწი რიცხვების სია 2-დან 10-მდე
evens = [x for x in range(2, 11) if x % 2 == 0]
print("ლუწი რიცხვები:", evens)  # [2, 4, 6, 8, 10]

# 34) გაფილტრე კენტი რიცხვები სიიდან
numbers = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in numbers if x % 2 != 0]
print("კენტი რიცხვები:", odds)  # [1, 3, 5, 7]

# 35) სტრინგების სია გადაყვანილი დიდი ასოებით
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("დიდი ასოებით:", uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']

# 36) კვადრატში ავიყვანოთ მხოლოდ ის რიცხვები სიიდან, რომლებიც იყოფა 2-ზე
nums = [1, 2, 3, 4, 5, 6]
squared_evens = [x**2 for x in nums if x % 2 == 0]
print("ლუწი რიცხვების კვადრატები:", squared_evens)  # [4, 16, 36]
# 37) მომხმარებლისთვის მისალმების ფუნქცია
def greet(name):
    print("გამარჯობა, " + name + "!")

greet("ნიკოლოზ")

# 38) ორი რიცხვის შეკრების ფუნქცია
def add_numbers(a, b):
    return a + b

print("შედეგი:", add_numbers(5, 3))  # 8

# 39) ფუნქცია რომელიც ამოწმებს ლუწია თუ კენტი
def check_even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

print(check_even_or_odd(7))  # კენტი

# 40) მართკუთხედის ფართობის გამოთვლა
def rectangle_area(length, width):
    return length * width

print("ფართობი:", rectangle_area(5, 4))  # 20

# 41) სტრინგის შებრუნების ფუნქცია
def reverse_string(text):
    return text[::-1]

print("შებრუნებული ტექსტი:", reverse_string("Python"))  # nohtyP
# 42) შექმენი და დაბეჭდე tuple
my_tuple = (10, "Hello", 3.14)
print("Tuple:", my_tuple)

# 43) tuple-ის მეორე ელემენტზე წვდომა
my_tuple2 = (1, 2, 3, 4, 5)
print("მეორე ელემენტი:", my_tuple2[1])  # 2

# 44) tuple-ის სიგრძის გამოთვლა
my_tuple3 = ("apple", "banana", "cherry")
print("Tuple-ის სიგრძე:", len(my_tuple3))  # 3

# 45) ორი tuple-ის შეკრება
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("შედგენილი tuple:", concatenated_tuple)  # (1, 2, 3, 4, 5, 6)

# 46) გადამოწმება თუ tuple-ში არსებობს კონკრეტული ელემენტი
my_tuple4 = ("apple", "banana", "cherry")
if "banana" in my_tuple4:
    print("მომძებნილი ელემენტი აღმოჩნდა!")
else:
    print("მომძებნილი ელემენტი არ არსებობს.")
# 47) შექმენი და დაბეჭდე set
my_set = {1, "apple", 3.14}
print("Set:", my_set)

# 48) გადამოწმება თუ ელემენტი არსებობს set-ში
my_set2 = {1, 2, 3, 4, 5}
if 3 in my_set2:
    print("Yes")
else:
    print("No")

# 49) ახალი ელემენტის დამატება set-ში
my_set3 = {"apple", "banana", "cherry"}
my_set3.add("orange")
print("განახლებული set:", my_set3)

# 50) ელემენტის ამოშლა set-დან
my_set4 = {"apple", "banana", "cherry"}
my_set4.remove("banana")
print("განახლებული set:", my_set4)

# 51) ორი set-ის გაერთიანება
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("გაერთიანებული set:", union_set)  # {1, 2, 3, 4, 5}
# 52) შექმენი და დაბეჭდე dictionary
my_dict = {"name": "ნიკოლოზ", "age": 25}
print("Dictionary:", my_dict)

# 53) მნიშვნელობის წვდომა კონკრეტული გასაღების მიხედვით
my_dict2 = {"name": "გიორგი", "city": "თბილისი", "age": 30}
print("name-ის მნიშვნელობა:", my_dict2["name"])  # გიორგი

# 54) ახალი key-value წყვილის დამატება dictionary-ში
my_dict3 = {"name": "თომა", "age": 22}
my_dict3["city"] = "ბათუმი"  # ახალი წყვილის დამატება
print("განახლებული dictionary:", my_dict3)

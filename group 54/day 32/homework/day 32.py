from turtle import *
# #
# def sum_of_two_numbers(num1, num2):
#     result = num1 + num2
#     print("The sum of", num1, "and", num2, "is", result)


# sum_of_two_numbers(3, 5)
# sum_of_two_numbers(10, 20)
# sum_of_two_numbers(7, 8)
# sum_of_two_numbers(15, 25)
# sum_of_two_numbers(100, 200)

def reverse_string(s):
    reversed_s = s[::-1]
    print(reversed_s)

reverse_string("გამარჯობა")
reverse_string("Hello")
reverse_string("Python")
reverse_string("Function")
reverse_string("String")

def find_maximum(numbers):
    max_value = max(numbers)
    print("The maximum value is", max_value)

find_maximum([1, 2, 3, 4, 5])
find_maximum([10, 20, 30, 40, 50])
find_maximum([7, 8, 9, 10, 11])
find_maximum([15, 25, 35, 45, 55])
find_maximum([100, 200, 300, 1000, 500])

    
# # ფუნქცია და მისი უპირატესობები
# ფუნქცია არის კოდის ბლოკი, რომელიც ასრულებს კონკრეტულ დავალებას. ფუნქციების გამოყენება საშუალებას გვაძლევს გავამარტივოთ და გავაუმჯობესოთ კოდის სტრუქტურა, გავზარდოთ მისი წაკითხვის და მართვის სიმარტივე, და თავიდან ავიცილოთ კოდის დუბლირება.
# def: ეს არის საკვანძო სიტყვა, რომელიც გამოიყენება ფუნქციის განსაზღვრისთვის. მაგალითად:
# def greet(name):
#     print("გამარჯობა", name)
# function name: ეს არის ფუნქციის სახელი, რომელიც გამოიყენება მისი გამოძახებისას. მაგალითად, ზემოთ მოცემულ მაგალითში, ფუნქციის სახელი არის greet.
# function parameter: ეს არის ცვლადი, რომელიც ფუნქციას გადაეცემა და რომლის მეშვეობითაც ფუნქცია იღებს მონაცემებს. მაგალითად, name არის პარამეტრი ფუნქციაში greet.
# indentation: ეს არის კოდის ხაზების გადატანა მარცხნიდან მარჯვნივ, რათა აღინიშნოს კოდის ბლოკი. პითონში, ინდენტაცია აუცილებელია კოდის სტრუქტურისთვის. მაგალითად:
# def greet(name):
#     print("გამარჯობა", name)
# code block: ეს არის კოდის ხაზების ჯგუფი, რომელიც შესრულდება ერთად. ფუნქციის შემთხვევაში, კოდის ბლოკი იწყება def საკვანძო სიტყვით და მოიცავს ყველა ინდენტირებულ ხაზს.
# function call: ეს არის ფუნქციის გამოძახება მისი სახელის და საჭირო არგუმენტების გამოყენებით. მაგალითად:
# greet("ნინო")
# function argument: ეს არის მონაცემები, რომლებიც გადაეცემა ფუნქციას გამოძახებისას. მაგალითად, ნინო არის არგუმენტი ფუნქციაში greet.
#            my ahh speeling
def draw_scuar (x,y):
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(100)
        right(90)

draw_scuar(100,-300)
draw_scuar(100,100)
draw_scuar(-300,100)
draw_scuar(-300,-300)
exitonclick()

#i got it working finallyyyy
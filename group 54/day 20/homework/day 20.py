# for ციკლი გვეხმარება ავტომატურად გავიმეოროთ ოპერაციები. მაგალითად, თუ გვინდა მივიღოთ რიცხვების ჩამონათვალი 1-დან 10-მდე, for ციკლი ძალიან გამოგვადგება ეს არის ცვლადი, რომელსაც for ციკლი იყენებს მნიშვნელობების განსაზღვრავად თითოეულ ეტაპზე. მაგალითად, როცა for ციკლი დაიწყებს, იგი საიტერაციო ცვლადს მისცემს საწყის მნიშვნელობას, შემდეგ კი ყოველ მომდევნო ეტაპზე შეცვლის მნიშვნელობას eეს არის ცვლადი, რომელსაც for ციკლი იყენებს მნიშვნელობების განსაზღვრავად თითოეულ ეტაპზე. მაგალითად, როცა for ციკლი დაიწყებს, იგი საიტერაციო ცვლადს მისცემს საწყის მნიშვნელობას, შემდეგ კი ყოველ მომდევნო ეტაპზე შეცვლის მნიშვნელობას.
for x in range(10,30):
    print(x)

for x in range(20,41):
    print(x)

for x in range(50,61,2):
    print(x)

for x in range(11,50,2):
    print(x)

number_sum=0
for x in range(10,30):
    number_sum=number_sum+x
print(number_sum)

number_sum=0
for x in range(2,30,2):
    number_sum=number_sum+x
print(number_sum)

for x in range(2,30,2):
    print(x)
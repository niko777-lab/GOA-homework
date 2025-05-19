
strings = ['apple', 'banana', 'cherry']
uppercased = list(map(str.upper, strings))
print("Uppercased:", uppercased)


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)


added_five = list(map(lambda x: x + 5, numbers))
print("Added 5:", added_five)

celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Fahrenheit:", fahrenheit)


words = ['hello', 'world', 'python', 'map']
first_chars = list(map(lambda w: w[0], words))
print("First characters:", first_chars)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

long_words = list(filter(lambda w: len(w) > 5, strings))
print("Strings longer than 5:", long_words)

nums = [10, -3, 5, -7, 8, 0]
non_negative = list(filter(lambda x: x >= 0, nums))
print("Non-negative numbers:", non_negative)

names = ['Alice', 'Bob', 'Anna', 'Mike', 'Andrew']
a_names = list(filter(lambda n: n.startswith('A'), names))
print("Names starting with 'A':", a_names)

div_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Numbers divisible by 3:", div_by_3)
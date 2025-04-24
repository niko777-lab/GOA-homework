# 1. Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# 2. Filter even numbers from a list of numbers 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# 3. Convert a list of lowercase words to uppercase
words = ["apple", "banana", "cherry", "date"]
uppercase_words = [word.upper() for word in words]

# 4. Get lengths of words in a list
word_lengths = [len(word) for word in words]

# 5. Add 5 to each number in a list
numbers = [1, 2, 3, 4, 5]
numbers_plus_5 = [x + 5 for x in numbers]

# 6. Get first letters from a list of strings
strings = ["apple", "banana", "cherry", "date"]
first_letters = [string[0] for string in strings]

# 7. Double each number in a given list
doubled_numbers = [x * 2 for x in numbers]

print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Uppercase words:", uppercase_words)
print("Word lengths:", word_lengths)
print("Numbers plus 5:", numbers_plus_5)
print("First letters:", first_letters)
print("Doubled numbers:", doubled_numbers)

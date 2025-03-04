# 1)
def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# მაგალითი
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_even_numbers(numbers_list))  # შედეგი: 30

# 2)
def sum_of_odd_squares(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total ** 2

# მაგალითი
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_odd_squares(numbers_list))  # შედეგი: 625

# 3)
def process_numbers(numbers):
    even_arr = []
    odd_arr = []
    for num in numbers:
        if num % 2 == 0:
            even_arr.append(num)
        else:
            odd_arr.append(num)
    
    sum_even = sum(even_arr)
    sum_odd = sum(odd_arr)
    
    result = sum_even * sum_odd
    return result

# მაგალითი
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(process_numbers(numbers_list))  # შედეგი: 165


# codewars:
# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)
# Remove String Spaces
def no_space(x):
    result = ""
    for i in x:
        if i != " ":
            result += i
    return result

# Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"

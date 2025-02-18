def baisc ():
    print("Hello,world!")
# calling funcion
baisc()

def two_num_sum(num1,num2):
    print(num1 + num2)

# calling funcion
two_num_sum(6,9)

def num_input(user_input):
    return user_input * 10

user_input = int(input("Enter Number"))

# calling funcion
print(num_input(user_input))

def name_greeting (name="Guest"):
    print("Hi there" + " " + name + "!")
# calling funcion
name_greeting()

def outer_function():
    print("This is the outer function.")
    
    def inner_function():
        print("This is the inner function.")
    
    # Calling the inner function
    inner_function()

# calling funcion
outer_function()

def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Example usage:
check_even_odd([1, 2, 3, 4, 5, 6])

def find_max(numbers):
    max_num = numbers[0]  # Start with the first number as the maximum
    
    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    
    return max_num

# Example usage:
result = find_max([10, 20, 4, 45, 99])
print("The maximum number is:", result)

def filter_positive_numbers(numbers):
    positive_numbers = []
    
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)  # Add positive numbers to the new list
    
    return positive_numbers

# Example usage:
result = filter_positive_numbers([-10, 5, -3, 7, 0, 2])
print("Positive numbers:", result)

def sum_divisible_by_3():
    total_sum = 0
    
    for num in range(1, 101):  # Iterate through numbers from 1 to 100
        if num % 3 == 0:
            total_sum += num  # Add numbers divisible by 3 to the sum
    
    return total_sum

# Example usage:
result = sum_divisible_by_3()
print("The total sum of numbers divisible by 3 is:", result)

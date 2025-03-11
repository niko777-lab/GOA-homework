# Convert a String to a Number!

def string_to_number(s):
    return int(s)

# Grasshopper - Summation
def summation(num):
    result=0
    for i in range(1,num+1):
        result=result+i
    return  result

# Function 1 - hello world
# Write a function `greet` that returns "hello world!"
def greet():
    return "hello world!"

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

# You Can't Code Under Pressure #1
def double_integer(i):
    return i *2

# Returning Strings
def greet(name):
    return f"Hello, {name} how are you doing today?"

# Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2


# Keep Hydrated!
def litres(time):
    return time // 2

# Century From Year
def century(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

# Convert number to reversed array of digits
def digitize(n):
    str_number = str(n)
    rev_number = str_number[::-1]

    new_list = []
    for number in rev_number:
        new_list.append(int(number))

    return new_list



# მოდი განვიხილოთ ეს მაგალითი
def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2

# ამ ფუნქციას აქვს 3 პარამეტრი operator, value1, value2
# if-ში გვეუბნებიან რომ თუ ოპერატორი უდრის "+" მიუმატოს value1 და value2
# elif-ში გვეუბნებიან რომ თუ ოპერატორი უდრის "-" გამოაკლოს value1-ერთს value2
# elif-ში გვეუბნებიან რომ თუ ოპერატორი უდრის "*" გამრავლოს value1  value2-ზე
# else-ში მეტი აღარ არის და არ უნდა  operator == "/" ის ავტომატურად გაკეთებს
# Beginner - Lost Without a Map
def maps(a):
    result = []
    for num in a:
        result.append(num * 2)
    return result


# Opposites Attract
def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True
    else:
        return False
# sum_array
def sum_array(a):
    return sum(a)

# Beginner Series #1 School Paperwork
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m
# MakeUpperCase
def make_upper_case(s):
    return s.upper()
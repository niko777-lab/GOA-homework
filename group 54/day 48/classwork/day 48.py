#Beginner - Lost Without a Map
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

# Sum Arrays
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

# Beginner Series #2 Clock
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000
# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == 'r' else f"{name} does not play banjo"
# Simple multiplication
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9
# Abbreviate a Two Word 
def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"
# A Needle in the Haystack
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"
# Invert values
def invert(lst):
    return [-x for x in lst]
#Calculate average
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
# Sentence Smash
def smash(words):
    return ' '.join(words)
# Beginner - Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
# Is he gonna survive?
def hero(bullets, dragons):
    return bullets >= dragons * 2

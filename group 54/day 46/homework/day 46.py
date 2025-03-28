# Create a tuple with at least 5 elements
my_tuple = (10, 20, 30, 40, 50)

# Extract the second element
second_element = my_tuple[1]

# Extract the last element
last_element = my_tuple[-1]

# Extract a slice of the middle three elements
middle_three = my_tuple[1:4]

print(second_element)
print(last_element)
print(middle_three)
tuble_test_Immutabe = ("niko" , "noone", True , False , 1,1,3,3)
# tuble_test_Immutabe[0] = "neon"
# what it returned
# aceback (most recent call last):
#   File "c:\Users\PC\Desktop\GOA\group 54\day 46\homework\day 46.py", line 17, in <module>
#     tuble_test_Immutabe[0] = "neon"
#     ~~~~~~~~~~~~~~~~~~~^^^

tuble1 = ("Nikoloz", "Iobidze" , 12 , 2012) 
Name,surname,age,year = tuble1
print(Name)
print(surname)
print(age)
print(year)
print(f"Hello my name is {Name} And my surname is {surname} I'am {age} years old and i was born in {year}")

tuble2 = (1,22,33,11,65,34,32,65)
print(tuble2.count([0]))
print(tuble2.index(1))


set1 = {"niko",12,2012,2025,"iobidze"}
set1.remove("niko")
set1.add("name")
print(set1)

list2 = [1,1,2,2,6,6,"niko","surname" ]

remove_Duplicates = list(set(list2))

print(remove_Duplicates)

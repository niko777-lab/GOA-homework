sentence = "I am learning Python and I love Python programming."
position = sentence.find("Python")
print("The first occurrence of the word 'Python' is at position:", position)
# Find
def user_specifed (index):
    for i in index:
        print(index[0])
user_specifed("nikolox")

def find_return (index):
    for i in index:
        print(index[0])

# count
def count_the(paragraph):
    print(paragraph.count("the"))
count_the("niko is the best acter and he is the best")

def count_character_occurrences(user_str, char):
    count = 0
    for c in user_str:
        if c == char:
            count += 1
    print("The character '{}' appears {} times in the given string.".format(char, count))

# მომხმარებლისგან სთრინგის და სიმბოლოს შემოტანა
user_str = input("შეიყვანეთ სთრინგი: ")
char = input("შეიყვანეთ სიმბოლო: ")

# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
count_character_occurrences(user_str, char)

def find_specified_word (word):
    print(word.count("no"))
find_specified_word("im no near the level of you")

# index 
def find_hello_index(input_string):
    index = input_string.find("hello")
    return index

# Example usage:
input_string = "Hi there, hello world!"
index = find_hello_index(input_string)
print(index)

def find_char_index(input_string, char):
    index = input_string.find(char)
    return index

# Example usage:
input_string = "Hello, world!"
char = "o"
index = find_char_index(input_string, char)
print(index)
# islower
def check_islower(string):
    print(string.islower())
check_islower("nikoloziobidzze")

def completely_islower (string):
    print(string.islower())
# Example usage:
completely_islower("IS thIS lOwEr case") #output fasle
completely_islower("is lower case") #output true

def check_lowercase():
    input_string = input("Please enter a string: ")
    
    if input_string.islower() and input_string.isalpha():
        print("The string contains only lowercase letters.")
    else:
        print("The string contains characters other than lowercase letters.")
        
# Example usage
check_lowercase()

# isupper
def verify_isupper(user_provider):
    print(user_provider.isupper())
user_provider=input("enter in uppercase")
verify_isupper(user_provider)
def is_uppercase(input_string):
    return input_string.isupper() and input_string.isalpha()

# Example usage:
result = is_uppercase("HELLO")
print(result)  # Output: True

result = is_uppercase("Hello")
print(result)  # Output: False

result = is_uppercase("HELLO123")
print(result)  # Output: False
def check_uppercase():
    input_string = input("Please enter a string: ")
    
    if input_string.isupper():
        print("The string is in uppercase.")
    else:
        print("The string is not in uppercase.")
        
# Example usage
check_uppercase()

def caluceltor(num1, num2, ოპერატორი):
    if ოპერატორი == '+':
        print(num1 + num2)
    elif ოპერატორი == '-':
        print(num1 - num2)
    elif ოპერატორი == '*':
        print(num1 * num2)
    elif ოპერატორი == '/':
        print(num1 / num2)
    else:
        print('არასწორი ოპერატორი')

# ფუნქციის გამოძახება სამჯერ, განსხვავებული არგუმენტებით
caluceltor(5, 3, '+')  
caluceltor(10, 4, '-')  
caluceltor(6, 2, '*')  
caluceltor(8, 2, '/')  


def find_minimum(user_list):
    minimum = user_list[0]
    for num in user_list:
        if num < minimum:
            minimum = num
    print(minimum)

# ფუნქციის გამოძახება ხუთჯერ, განსხვავებული სიებით
find_minimum([5, 3, 8, 1, 2])  
find_minimum([10, 20, 30, 5, 15])  
find_minimum([100, 50, 25, 75, 10])  
find_minimum([7, 14, 21, 3, 28])  
find_minimum([9, 6, 4, 2, 8])  

def manual_capitalize(user_str):
    user_str = user_str.lower()
    capitalized_str = user_str[0].upper() + user_str[1:]
    print(capitalized_str) 

user_input = input("შეიყვანეთ სთრინგი: ")

print(manual_capitalize(user_input))

def check_lowercase(user_str):
    if user_str.islower():
        print(user_str)

#  მომხმარებლისგან წინდადადების შემოტანა 
text = input("შეიყვანეთ წინდადება :")

# ფუნქცის გამოძახება და არგუმენტად  text ცვალდის გადაცემა

def iscapitalized(user_str):
    # შემოწმება, არის თუ არა პირაველი სმბოლო uppercase და დანარჩენი სიმბოლოები lowercase
    if user_str[0].isupper() and user_str[1:].islower():
        print(True)
    else:
        print(False)

text1= input("შეიყვანეტ წინდადადება:")
iscapitalized(text1)

def manual_isdigit(user_str):
    is_digit = True
    for char in user_str:
        if char not in "0123456789":
            is_digit = False
    print(is_digit)

# მომხმარებლისგან შემოტანილი სთრინგი
text2=str(input("შეიყვანეთ სთრინგი"))

manual_isdigit(text2)

def split_sentenc(user_str):
    split_list = user_str.split(" ")
    print(split_list)

text3 = input("შეიყვანე ტექსტი:")

split_sentenc(text3)
correct_num = 10
user_input = int(input("შემოიტანეთ მთელი რიცხვი: "))

while user_input != correct_num:
    print("არასწორი, სცადეთ თავიდან")
    user_input = int(input("შემოიტანეთ მთელი რიცხვი: "))

print("correct guess")

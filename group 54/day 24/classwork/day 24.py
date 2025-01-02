# user_num=int(input("enter number"))
# if user_num > 10:
#     print("bigger than 10")
# else:
#     print("smaller than 10")

# მომხმარებლისგან ინფორმაციის შემოტანა
user_input = input("Are you a student? (yes/Yes): ")

# is_student ცვლადის შექმნა და მნიშვნელობის მინიჭება
if user_input == "yes" or user_input == "Yes":
    is_student = True
else:
    is_student = False

print("Is student:", is_student)

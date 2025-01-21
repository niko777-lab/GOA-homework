# # სიის შექმნა 10 ელემენტით
# my_list = ["apple", "banana", 3.14, 2.71, 42, 7, True, False, [1, 2, 3], ["a", "b", "c"]]

# # slicing ორი რიცხვის გადაცემით
# list_1 = my_list[2:7]
# print("Sliced list with two numbers:",list_1)

# # slicing სამი რიცხვის გადაცემით
# list_2 = my_list[1:9:2]
# print("Sliced list with three numbers:", list_2)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# reversed_list = my_list[::-1]
# print( reversed_list)

# slice1 = my_list[2:5]  # [3, 4, 5]
# slice2 = my_list[0:10]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# slice3 = my_list[5:15]  # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# slice4 = my_list[7:12]  # [8, 9, 10, 11, 12]
# slice5 = my_list[10:14]  # [11, 12, 13, 14]


# print(slice1)
# print(slice2)
# print(slice3)
# print(slice4)
# print(slice5)


# slice1 = my_list[0:10:2]  # [1, 3, 5, 7, 9]
# slice2 = my_list[1:15:3]  # [2, 5, 8, 11, 14]
# slice3 = my_list[2:12:4]  # [3, 7, 11]
# slice4 = my_list[3:15:5]  # [4, 9, 14]
# slice5 = my_list[4:14:3]  # [5, 8, 11, 14]


# print(slice1)
# print(slice2)
# print(slice3)
# print(slice4)
# print(slice5)


# slice1 = my_list[5:]  # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# slice2 = my_list[:10]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# slice3 = my_list[7:]  # [8, 9, 10, 11, 12, 13, 14, 15]
# slice4 = my_list[:5]  # [1, 2, 3, 4, 5]
# slice5 = my_list[10:]  # [11, 12, 13, 14, 15]


# print(slice1)
# print(slice2)
# print(slice3)
# print(slice4)
# print(slice5)



# ახალი 10 ელემენტოანი სია

list = [1,2,3,4,5,6,7,8,9,10]

# 10 ელემენტიანი სია
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# slicing-ის მაგალითები უარყოფითი ინდექსებით
example_1 = my_list[-10:-5]  # [1, 2, 3, 4, 5]
example_2 = my_list[-8:-3]   # [3, 4, 5, 6, 7]
example_3 = my_list[-6:-1]   # [5, 6, 7, 8, 9]
example_4 = my_list[-5:]     # [6, 7, 8, 9, 10]
example_5 = my_list[-7:-2]   # [4, 5, 6, 7, 8]

print(example_1)
print(example_2)
print(example_3)
print(example_4)
print(example_5)
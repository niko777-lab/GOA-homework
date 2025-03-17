tuple1 = (1,23,13,532,1223,)

print(min(tuple1))
print(max(tuple1))
print(tuple1.count(tuple1[0]))

def no_duplicates(user_list):
    return list(set(user_list))

list_1 = [1, 2, 2, 3, 4, 4, 5]
list_2 = ['a', 'b', 'a', 'c', 'd', 'd']
list_3 = [True, False, True, False, True]

print(no_duplicates(list_1))
print(no_duplicates(list_2))
print(no_duplicates(list_3))
dishes = ["Salad", "BBQ", "Spaghetti"]
guests = {"Mery", "Anna", "Jonathan"}
print(dishes[0])
print(guests[0])
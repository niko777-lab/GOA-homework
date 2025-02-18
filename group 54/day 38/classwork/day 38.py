def remove_one_element (index,list):
    print(list.pop(index))

remove_one_element(1,[1,2,3,4,5,6,7])
def remove_one_element(my_list, index):
    # გამოიყენეთ .pop() მეთოდი ინდექსზე ელემენტის ამოსაღებად
    my_list.pop(index)
    print(my_list)

# მაგალითი
remove_one_element([1, 2, 3, 4, 5], 2)

def square (user_num):
    return user_num * user_num

squar = square(5)
print(squar)
print(squar*2)
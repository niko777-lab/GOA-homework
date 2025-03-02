def max_num(arr):
    # first option
    # return max(arr)
    # secend option 
    for number in arr:
        max_number = arr[0]
        if number > max_number:
            max_number = number

print(max_num[1,2,4,0,76,9786,58,])
# first option
def max_number(numbers):
    return max(numbers)

# secend option

def sum_of_squares_of_positives(numbers):
    return sum(x**2 for x in numbers if x > 0)

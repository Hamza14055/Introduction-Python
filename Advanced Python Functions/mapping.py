list_1 = [1,2,3,4,5]
list_2 = [9,8,7,6,5]
result = map(lambda x,y : x+y ,list_1,list_2)
print("The result of the addition is ",list(result))

square_list = [1,2,3,4,5,6]
def square (n):
    result = n*n
    return result
for numbers in square_list:
    print(square(numbers))
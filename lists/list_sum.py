my_list =[7,4,5,6,3,2,1,4]
sum = 0 
for i in my_list:
    sum+=i
print(sum)
length = len(my_list)
average = sum/length
print(average)
my_list.sort()
print(my_list)
max = my_list[-1]
print("max number is ",max)
smallest = my_list[0]
print("smallest number is ",smallest)
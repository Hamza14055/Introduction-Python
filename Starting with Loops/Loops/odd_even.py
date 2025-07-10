Num = [1,2,3,4,5,6,7,8,9,10]
even =[]
odd=[]
for Numbers in Num:
    if Numbers%2==0:
        even.append(Numbers)
    elif Numbers%2 != 0:
        odd.append(Numbers)
print(even)
print(odd)



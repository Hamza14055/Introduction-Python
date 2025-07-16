dic1 = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
value = 1
count = 0
for key in dic1:
    if dic1[key] == value:
        count+=1
print("Frequency of ",value,"is",count)
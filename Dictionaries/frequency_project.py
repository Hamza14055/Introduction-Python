frequency = int(input("Enter which number's frequency you want "))
test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}
count = 0
for key in test_dict:
    if test_dict[key] == frequency:
        count+=1
print("frequency of ",frequency,"is",count)
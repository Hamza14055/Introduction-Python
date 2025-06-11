string = input("Enter the Word : ")
char = input("Enter the Character : ")
count = 0
i = 0
while i < len(string):
    if (string[i]==char):
        count = count+1
    i = i+1
print("This character occured",count,"times")
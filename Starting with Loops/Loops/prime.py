num = int(input("Enter the 1st Number : "))
num_2 = int(input("Enter the last Number : "))
count = 0
for i in range (num,num_2+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0 :
                break
        else :
            print(i)
    

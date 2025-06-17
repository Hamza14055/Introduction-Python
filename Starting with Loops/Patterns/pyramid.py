Num = int(input("Enter a Number : "))
i = 1
while i<=Num:
    space=Num-i
    while space>0:
        print(" ",end='')
        space-=1
    star =1
    while star<=i:
        print("**",end='')
        star+=1
    print()
    i+=1






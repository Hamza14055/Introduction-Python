Num = int(input("Enter a Number : "))
i = Num
n = 1
while i>=1:
    space=0
    while space<Num-i:
        print(" ",end='')
        space+=1
    star = 0
    while star<(2*i-1):
        print(n,end='')
        star+=1
    print()
    i-=1
    n+=1
    
Row_size = int(input("Enter number of rows "))
if Row_size%2 == 0:
    half_diam=Row_size//2
else :
    half_diam=(Row_size//2)+1
space = half_diam-1
for i in range(1,half_diam+1):
    for j in range(space):
        print(" ",end="")
    space -=1
    num = 1
    for j in range(2*i-1):
      print(num,end='')
      num+=1
    print()
space = 1
for i in range(1,half_diam):
    for j in range(space):
        print(" ",end="")
        space+=1
    num = 1
    for j in range(2*(half_diam-i)-1):
        print(num,end="")
        num+=1
    print()


    


        
Num = int(input("Enter a Number : "))
if Num%20 == 0:
    print("Twist")
elif Num%15 == 0:
    pass
elif Num%5 == 0:
    print("Fizz")
elif Num%3==0:
    print("buzz")
else:
    print(Num)
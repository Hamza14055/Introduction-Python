def Factorial(Num):
    if Num == 1 or Num ==0:
        return 1
    else:
        return Num*Factorial(Num-1)
    
Num = int(input("Enter a Number : "))
if Num<0:
    print("The factorial doesnot exist for negative numbers ")
else:
    print(f"The factorial of {Num} is",Factorial(Num))
a = int(input("Enter the first Number : "))
b = int(input("Enter the second Number : "))
Function = input("Which operation do you want to perform(+,-,/,*)")
def add (a,b):
    c = a+b
    return c
def multiply (a,b):
    c=a*b
    return c
def divide (a,b):
    c=a/b
    return c
def subtract (a,b):
    c=a-b
    return c
if Function == "+":
    print(a,"+",b,"=",add(a,b))
elif Function == "-":
    print(a,"-",b,"=",subtract(a,b))
elif Function == "*":
    print(a,"x",b,"=",multiply(a,b))
elif Function == "/":
    print(a,"/",b,"=",divide(a,b))
else:
    print("PLease enter a valid operator ")





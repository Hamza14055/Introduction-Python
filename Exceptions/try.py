try:
    Num = int(input("Enter a Number : "))
    print("The Number is ",Num)
except ValueError as ex:
    print("Exception :",ex)


print("I am outside of the try block")

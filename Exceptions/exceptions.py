try:
    Num1 = int(input("Enter a number : "))
    Num2 = int(input("Enter the second number : "))
    Division = Num1/Num2
    print(Division)
except ZeroDivisionError as ex:
    print("Dividing by zero is not possible ")
except ValueError as ex:
    print("Enter a Valid Number ")
except NameError as ex:
    print("The error is",ex)
except:
    print("An error has occured ")
finally:
    print("The program will run regardless of any error")
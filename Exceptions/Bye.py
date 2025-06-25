valid = False
try:
 while not valid:
    n = int(input("Enter a Number "))
    while n%2==0:
        print("bye")
except ValueError:
   print("Invalid value entered")

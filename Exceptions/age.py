Valid = False
try:
    while not Valid :
        n = int(input("Enter your age "))
        if n%2 == 0 and n>0:
            print(f"The age",n," is even and a real integer")
except ValueError:
    print("incorrect value entered")
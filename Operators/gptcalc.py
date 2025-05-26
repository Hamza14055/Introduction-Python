A = int(input("Which number do you want to calculate? "))
B = int(input("What is the other number? "))
C = input("What do you want to do (+, -, x, /)? ")

if C == "+":
    D = A + B
    print(D)
elif C == "-":
    D = A - B
    print(D)
elif C == "x":
    D = A * B
    print(D)
elif C == "/":
    if B != 0:
        D = A / B
        print(D)
    else:
        print("Cannot divide by zero.")
else:
    print("please write the right operator.")

print("Number Calculated")
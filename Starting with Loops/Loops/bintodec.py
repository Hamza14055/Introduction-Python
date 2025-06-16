A = int(input("Enter the Number "))
Binary = ""
while A > 0:
    Remainder = A%2
    Binary = str(Remainder) + Binary
    A = A//2
print(Binary)

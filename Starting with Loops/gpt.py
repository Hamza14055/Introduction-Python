Num = int(input("Enter the Number : "))
digits = 0

# Handle the case when number is 0
if Num == 0:
    digits = 1
else:
    while Num != 0:
        Num = Num // 10
        digits += 1

print("Number of digits:", digits)

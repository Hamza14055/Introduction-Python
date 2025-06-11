Num = input("Enter the Number : ")
if len(Num)<4:
    print("enter a number with 4 digits")
else:
    digits= []
    for i in Num :
        digits.append(int(i))
    length = len(digits)
    mid_digit_1 = length//2 - 1
    mid_digit_2 = length//2
    mid_1 = digits[mid_digit_1]
    mid_2 = digits[mid_digit_2]
    product = mid_1 * mid_2
    print("The product of the middle numbers is ", product)
Num = int(input("Enter the Number : "))
Sum = 0
temp = Sum
while temp >0 :
    digit = temp%10
    sum = (sum+digit**3)
    temp//=10
if Num == sum:
    print("It is an armstrong number")
else:
    print("Its not an armstrong number ")
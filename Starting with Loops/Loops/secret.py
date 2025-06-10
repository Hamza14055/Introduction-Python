secret = 123
attempts = 0
Num = int(input("Enter your guess number "))
while secret != Num:
    if Num>secret:
        print("You are higher ! ")
    elif Num < secret :
       print("You are lower ! ")
    Num = int(input("Try again : "))
    attempts = attempts+1
    print("attempt number " , attempts)
else :
 print("Yes you are correct !!! ")

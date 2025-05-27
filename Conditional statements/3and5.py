Num = int(input("Which Number do you want to check ? "))
if Num%3 == 0 and Num%5 == 0 :
    print(Num,"is both divisible by 3 and 5")
elif Num%3 == 0 and Num%5 != 0 :
    print(Num,"is only divisible by 3 ")
elif Num%3 != 0 and Num%5 == 0 :
    print(Num,"is only divisible by 5")
    

    
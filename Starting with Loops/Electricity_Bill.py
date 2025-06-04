Units = int(input("How many Units did You use ? "))
if Units < 50 :
    print("Your electricity bill is :",Units*2.60+25)
elif Units > 50 :
    if Units<=100 :
        print("The cost is ",Units*3.25+35)
    elif Units > 100 :
        if Units < 200 :
            print("The cost is " , Units*5.26+45)
        else :
            print("The cost is " , Units*8.45+75 )

    
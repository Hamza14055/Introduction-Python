Buy = int(input("For how much did You buy the product ? "))
Sell = int(input("For how much did You sell it ? "))
if (Sell-Buy) > 0 :
    print ("You just made a profit")
    print ("The Profit is ",(Sell-Buy))
elif (Sell-Buy) < 0 :
    print ("You just had a loss ")
    print ("The loss was of ",(Buy-Sell))

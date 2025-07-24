list_1 = [1,2,3,4,5,6]
list_2 = [7,8,9,10,11,12]
for x , y in zip(list_1,list_2[::-1]):
    print(x,y)
Stocks = ["Reliance","Engro","Honda"]
Prices = [2000,300,900]
dict_1 = {Stocks: Prices for Stocks,Prices in zip(Stocks,Prices)}
print(dict_1)
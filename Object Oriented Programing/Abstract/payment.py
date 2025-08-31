from abc import ABC,abstractmethod
class Payment():
    def Pay(self,Ammount):
        pass
class Credit_Card():
    def Pay(self,Ammount):
        print("You are now paying",Ammount, "through credit card ")
class UPI():
    def Pay(self,Ammount):
        print("You are paying " ,Ammount,"using UPI ")
C = Credit_Card()
U = UPI()
Option = input("What payment method do you want Credit Card or UPI C/U ")
Ammount = int(input("Enter the Ammount : "))
if Option.upper() == "C":
    C.Pay(Ammount)
else:
    U.Pay(Ammount)

 
    
class Device:
    def __init__(self,brand):
        self.brand = brand
class Phone(Device):
    def __init__(self, brand,price):
        self.price= price 
        super().__init__(brand)
    def display(self):
        print("The brand is ",self.brand)
        print("The price is ",self.price)
Iphone = Phone("Apple",240000)
Iphone.display()
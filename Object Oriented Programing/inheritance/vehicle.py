class vehicle :
    def __init__(self,name,speed,mileage):
        self.name = name 
        self.speed = speed 
        self.mileage = mileage

class bus(vehicle):
    pass 
obj = bus("Yutong",180,11)
print("Bus name",obj.name)
print("Bus speed",obj.speed)
print("Bus Mileage",obj.mileage)


        
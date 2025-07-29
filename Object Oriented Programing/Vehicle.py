class vehicle:
    def __init__(self,Max_speed,mileage):
        self.Max_speed = Max_speed
        self.mileage = mileage
Car = vehicle(60,13)
print("Maximum speed of the vehicle is " ,Car.Max_speed)
print("The mileage of this vehicle is ",Car.mileage)
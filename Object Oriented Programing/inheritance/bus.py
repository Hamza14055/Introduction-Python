class vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
        
    def fare_calculation(self):
        fare_1 = self.seating_capacity*100 
        fare = 10/100*fare + fare_1
class bus(vehicle):
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity

    def fare_calculation(self):
        fare_1 = self.seating_capacity*100 
        fare_2 = 10/100*fare_1
        fare = fare_2+fare_1
        print("The fare is ",fare)
obj = bus(50)
obj.fare_calculation()
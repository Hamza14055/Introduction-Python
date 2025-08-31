class BMW():
    def max_speed(self):
        print("The max speed is 250km/h")
    def fuel_type(self):
        print("The fuel must be unleaded ")
class Ferrari():
    def max_speed(self):
        print("The Max speed is 300 km/h")
    def fuel_type(self):
        print("High octane fuel is required ")
B = BMW()
F = Ferrari()
for cars in (B,F):
    cars.fuel_type()
    cars.max_speed()

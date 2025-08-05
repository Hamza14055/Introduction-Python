class circle :
    def __init__(self,radius):
        self.radius = radius 
    def circumference(self):
        return 2*3.14*self.radius
circ = circle(6)
print(circ.circumference())
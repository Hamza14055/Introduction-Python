class Circle:
    def __init__(self, radius):
        self.radius = radius
        area = 3.14 * (radius ** 2)
        circumference = 2 * 3.14 * radius
        print("Area:", area)
        print("Circumference:", circumference)

radius = int(input("Enter the radius: "))
c = Circle(radius)


    
    
        
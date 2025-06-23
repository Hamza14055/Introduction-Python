Shape = input("Enter the shape(square/rectange) ")
length = int(input("Enter the length "))
width = int(input("Enter the width "))
def perimeter_square (length):
    perimeter = length*4
    return perimeter
def perimeter_rectangle (length,width):
    perimeter = 2*(length+width)
    return perimeter
if Shape.lower() == "square" :
    print("The perimeter is : ",perimeter_square(length))
elif Shape.lower() == "rectangle":
    print("The perimeter is ",perimeter_rectangle(length,width))
else:
    print("Please enter a valid shape")
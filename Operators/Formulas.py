A = str(input("Which Shape's Area do you want to calculate ? "))
if A == ("circle") :
    B=int(input("What is the radius ? "))
    print ("The area of the circle is " ,(3.14*(B**2)))
if A == ("triangle") :
    C = int(input("What is the height ? "))
    D = int(input("What is the Base ? "))
    print ("The area of the triangle is ",(C*D)/2)
if A == ("square") :
    E = int(input("What is the length ? "))
    print ("The area of the square is ",(E**2))
if A == ("Rectangle") :
    F = int(input("What is the length ? "))
    G = int(input("What is the width ? "))
    print ("The area of the rectangle is ",(F*G))
if A == ("circle") :
    B=int(input("What is the radius ? "))
    print ("The area of the circle is " ,(3.14*(B**2)))
if A == ("triangle") :
    C = int(input("What is the height ? "))
    D = int(input("What is the Base ? "))
    print ("The area of the triangle is ",(C*D)/2)
if A == ("square") :
    E = int(input("What is the length ? "))
    print ("The area of the square is ",(E**2))
if A == ("rectangle") :
    F = int(input("What is the length ? "))
    G = int(input("What is the width ? "))
    print ("The area of the rectangle is ",(F*G))
if A == ("paralellogram") :
    H = int(input("What is the base ? "))
    I = int(input("What is the height ? "))
    print ("The area of the paralellogram is ",(H*I))

else : print("This program is not designed to calculate the area of this shape ")   
input("\nPress Enter to exit...")




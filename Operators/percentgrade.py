Sub_1 = int(input("Enter Maths Marks "))
Sub_2 = int(input("Enter English Marks "))
Sub_3 = int(input("Enter History Marks "))
Sub_4 = int(input("Enter Chemistry Marks "))
Sub_5 = int(input("Enter Physics Marks "))
Average = ((Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5)/500)*100
if Average<= 100 and Average>= 91 :
    print("You got an A2 grade")
elif Average<91 and Average>= 81 :
    print("You got an A1 grade")
elif Average<81 and Average>= 71 :
    print("You got a B2 grade")
elif Average<71 and Average>= 61 :
    print("You got a B1 grade ")
elif Average<61 and Average>= 51 :
    print("You got a C2 grade")
elif Average<51 and Average>= 41 :
    print("You got a C1 grade")
elif Average<41 and Average>= 31 :
    print("You got a D2 grade ")
elif Average<31 and Average>= 21 :
    print("You got a D1 grade ")
elif Average<21 and Average>= 11 :
    print("You got a E2 grade ")
elif Average<11 and Average>= 0 :
    print("You got a E grade ")
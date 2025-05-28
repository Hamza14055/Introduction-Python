base = int(input("What is the size of the base ? "))
side_2 = int(input("What is the size of the other side ? "))
side_3 = int(input("What is the size of the other side ? "))
if base == side_2 and base == side_3 and side_2 == side_3 :
    print("it is an equilateral triangle ")
elif base != side_2 and side_3 != base and side_3 == side_2 :
    print("It is an isoceles triangle ")
else :
    print("Its a scalene triangle ")
    

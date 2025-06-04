Medical = input("Do you have any medical cause? Y/N ")
if Medical == "Y" :
    print("You are allowed to take the exam ")
elif Medical == "N":
    Attendance = int(input("What was your attendance ? "))
    if Attendance > 75 :
        print("You are allowed to take the exam ")
    else :
        print("You are not allowed to take the exam ")
else :
    print("Enter the correct Value ")

    
    

Ride = input("Which mode do you want to use Car/Bike ")
if Ride == "Car":
    Choice = input("Do you want air conditioning Y/N ")
    if Choice == "Y" :
        print("Enjoy your ride ")
    else :
        print("Enjoy the heat ")
elif Ride == "Bike" :
    Choice_2 = input("Do you want a Honda or a Kwasaki ")
    if Choice_2 == "Kwasaki":
        print("Enjoy your speedy ride")
    else :
        print("Enjoy your ride with a Honda")
else :
    print("Please Enter only Car or Bike ")
Marks = int(input("What are your Marks ? "))
if Marks > 100 :
    print("Please enter marks less than 100")
else :
 if Marks > 0 and Marks < 40 :
    print ("You just got a D grade ")
 elif Marks >= 40 and Marks < 60 :
    print("You just got a C grade ")
 elif Marks >= 60 and Marks < 75 :
    print("You just got a B grade ")
 else : print("You just got an A grade")
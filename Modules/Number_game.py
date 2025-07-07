import random
playing = True
Number = str(random.randint(1,11))
while playing :
    Guess = input("Enter a Number between 1-10 : ")
    if Number == Guess:
            print("You are Correct!!")
            Leave = input("press any character to leave")
            break
    else:
          print("Guess again ")
          leave_2 = input("Press any other character to leave ")
        
        


import random
playing = True
Number = str(random.randint(1,11))
while playing :
    Guess = input("Enter a Number between 1-10 : ")
    if Number == Guess:
            print("You are Correct!!")
            break
    else:
          print("Guess again ")
        
        


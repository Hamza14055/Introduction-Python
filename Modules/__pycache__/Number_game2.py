import random 
print("This is a random number guessing game ")
guess = int(input("Guess a Number between 1-10 "))
random_number = random.randint(1,10)
while guess != random_number :
    guess= int(input("Try again!!! : "))
if guess == random_number :
    print("You are correct ")

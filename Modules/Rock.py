import random
playing = True
list = ['rock','paper','scissors']
computer_choice = random.choice(list)
while playing:
   Person_Choice = input("Choose (Rock/Paper/scissors)  ")
   if Person_Choice.lower() == computer_choice :
      print("Its a draw")
   elif Person_Choice.lower() == "rock" and computer_choice == "paper":
      print("You lost!!")
   elif Person_Choice.lower() == "paper" and computer_choice == "rock":
      print("You won!!")
   elif Person_Choice.lower() == "scissors" and computer_choice == "paper":
      print("You won!!")
   elif Person_Choice.lower() == "paper" and computer_choice =="scissors":
      print("You lost!!")
   elif Person_Choice.lower() == "scissors" and computer_choice=="rock":
      print("You lost")
   elif Person_Choice.lower() =="rock" and computer_choice=="scissors":
      print("You won!!")
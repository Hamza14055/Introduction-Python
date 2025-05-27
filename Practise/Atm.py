User = str(input("What is your username ? "))
Pin = str(input("What is your pin ? "))
if Pin == "Hamza123" and User == "Hamza" :
    Balance = int(input("How much money do you want to withdraw ? "))
    if Balance > 100000 :
        print("Insufficient Balance ! ")
    else :
        print("Transaction Successful ! ")
elif User != "Hamza" or Pin != "Hamza123" :
    print("Username or pin number is incorrect !!")

